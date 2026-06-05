import json
from pathlib import Path
import shlex

BASE_DIR = Path(__file__).resolve().parents[1]
from datetime import datetime
import subprocess

DATA_PATH = BASE_DIR / 'scripts' / '.cache' / 'runbook_v8_data.json'
OUT_PATH = BASE_DIR / 'docs' / 'runbooks' / 'Smart_Home_Runbook_v8.md'


def sh(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True).strip()
    except Exception:
        return ''


def md_table(headers, rows):
    out = []
    out.append('| ' + ' | '.join(headers) + ' |')
    out.append('| ' + ' | '.join(['---']*len(headers)) + ' |')
    for r in rows:
        rr = [str(x).replace('\n', ' ').replace('|', '\\|') for x in r]
        out.append('| ' + ' | '.join(rr) + ' |')
    return '\n'.join(out)


def main():
    data = json.loads(DATA_PATH.read_text())
    cfg = data['config']
    states = data['states']
    ws = data['ws']

    device_registry = ws['device_registry'].get('result', [])
    entity_registry = ws['entity_registry'].get('result', [])
    area_registry = {a['area_id']: a.get('name','') for a in ws['area_registry'].get('result', [])}
    dashboards = ws['dashboards'].get('result', [])
    integrations = ws['config_entries'].get('result', [])

    state_map = {s.get('entity_id'): s for s in states if isinstance(s, dict) and s.get('entity_id')}

    automations = sorted([s for s in states if isinstance(s, dict) and s.get('entity_id','').startswith('automation.')], key=lambda x: x['entity_id'])

    # Add-ons from supervisor WS probe (fresh)
    addons = []
    backups = []
    sup_info = {}
    probe_path = BASE_DIR / 'scripts' / '.cache' / 'supervisor_probe.json'
    if probe_path.exists():
        x = json.loads(probe_path.read_text())
        addons = x.get('addons', [])
        backups = x.get('backups', [])
        sup_info = x.get('info', {})

    # fallback from prior captured
    if not backups:
        b = data.get('hassio_backups', {}).get('backups', []) if isinstance(data.get('hassio_backups'), dict) else []
        backups = b

    now_local = sh('date "+%Y-%m-%d %H:%M:%S %Z"')
    tailscale_json = sh('/usr/bin/tailscale status --json')
    ts = {}
    if tailscale_json:
        try:
            ts = json.loads(tailscale_json)
        except Exception:
            ts = {}

    # NAS details. The current primary Kira host is macOS; keep Linux
    # automount details optional so this runbook can still be built from
    # Omarchy if needed.
    mac_nas_path = Path('/Volumes/Plex_HD')
    local_nas_path = mac_nas_path if mac_nas_path.exists() else Path('/home/tonmoy/nas')
    fstab = Path('/etc/fstab').read_text() if Path('/etc/fstab').exists() else ''
    nas_mount_unit = Path('/etc/systemd/system/home-tonmoy-nas.mount').read_text() if Path('/etc/systemd/system/home-tonmoy-nas.mount').exists() else ''
    nas_automount_unit = Path('/etc/systemd/system/home-tonmoy-nas.automount').read_text() if Path('/etc/systemd/system/home-tonmoy-nas.automount').exists() else ''
    nas_tree = sh(
        f"find {shlex.quote(str(local_nas_path))} "
        "\( -name .Trashes -o -name .Spotlight-V100 -o -name .TemporaryItems \) -prune "
        "-o -maxdepth 3 -mindepth 1 -type d -print | sort"
    ) if local_nas_path.exists() else ''

    lines = []
    lines.append('# Smart Home Operational Runbook v8')
    lines.append('')
    lines.append(f'- Generated: {now_local}')
    lines.append(f'- Source snapshot (UTC): {data.get("generated_at_utc", "unknown")}')
    lines.append('- Data sources: Home Assistant REST API, Home Assistant WebSocket registries, Supervisor API (WebSocket), local host NAS state, optional Linux systemd/fstab state, Tailscale status')
    lines.append('')

    lines.append('## System Overview')
    lines.append('')
    lines.append(md_table(['Field','Value'], [
        ['Home Assistant Name', cfg.get('location_name','')],
        ['HA Version', cfg.get('version','')],
        ['State', cfg.get('state','')],
        ['Config Source', cfg.get('config_source','')],
        ['Timezone', cfg.get('time_zone','')],
        ['Language', cfg.get('language','')],
        ['Country', cfg.get('country','')],
        ['Latitude / Longitude', f"{cfg.get('latitude')} / {cfg.get('longitude')}"] ,
        ['Components Loaded', len(cfg.get('components',[]))],
        ['Dashboards', len(dashboards)],
        ['Devices (registry)', len(device_registry)],
        ['Entities (state API)', len(states)],
        ['Entities (entity registry)', len(entity_registry)],
        ['Automations (entities)', len(automations)],
    ]))
    lines.append('')

    lines.append('## Network Architecture')
    lines.append('')
    lines.append('- Primary LAN inferred from live endpoints and routes: `192.168.50.0/24`')
    lines.append(f"- Home Assistant endpoint in use: `{cfg.get('internal_url') or 'http://192.168.50.166:8123 (from local HA env)'}`")
    lines.append('- Known key nodes (live + local config):')
    lines.append('  - Router/Gateway: `192.168.50.1`')
    lines.append('  - Mac Mini NAS/host: `192.168.50.208`')
    lines.append('  - HA endpoint used by Kira: `192.168.50.166:8123`')
    lines.append('  - Neo Blinds hub (documented): `192.168.50.224:8839`')
    lines.append('')

    lines.append('## Device Registry (all devices)')
    lines.append('')
    dev_rows = []
    for d in sorted(device_registry, key=lambda x: (x.get('name_by_user') or x.get('name') or x.get('id',''))):
        dev_rows.append([
            d.get('id',''),
            d.get('name_by_user') or d.get('name') or '',
            area_registry.get(d.get('area_id',''),''),
            d.get('manufacturer',''),
            d.get('model',''),
            ','.join(d.get('identifiers', [''])[0]) if d.get('identifiers') else '',
            str(d.get('disabled_by') or ''),
        ])
    lines.append(md_table(['Device ID','Name','Area','Manufacturer','Model','Primary Identifier','Disabled'], dev_rows))
    lines.append('')

    lines.append('## Entity Inventory (all entities)')
    lines.append('')
    domain_counts = {}
    for e in entity_registry:
        eid = e.get('entity_id','')
        if '.' in eid:
            domain = eid.split('.',1)[0]
            domain_counts[domain] = domain_counts.get(domain,0)+1
    lines.append('### Entity Domain Summary (entity registry)')
    lines.append('')
    lines.append(md_table(['Domain','Count'], [[k,v] for k,v in sorted(domain_counts.items())]))
    lines.append('')
    ent_rows = []
    for e in sorted(entity_registry, key=lambda x: x.get('entity_id','')):
        eid = e.get('entity_id','')
        st = state_map.get(eid, {}).get('state', 'unavailable_in_state_api')
        ent_rows.append([
            eid,
            st,
            e.get('platform',''),
            e.get('device_id',''),
            area_registry.get(e.get('area_id',''),''),
            str(e.get('disabled_by') or ''),
            str(e.get('hidden_by') or ''),
        ])
    lines.append(md_table(['Entity ID','State','Platform','Device ID','Area','Disabled By','Hidden By'], ent_rows))
    lines.append('')

    lines.append('## Integration List')
    lines.append('')
    int_rows = []
    for i in sorted(integrations, key=lambda x: (x.get('domain',''), x.get('title',''))):
        int_rows.append([
            i.get('entry_id',''),
            i.get('domain',''),
            i.get('title',''),
            i.get('state',''),
            i.get('source',''),
            str(i.get('disabled_by') or ''),
        ])
    lines.append(md_table(['Entry ID','Domain','Title','State','Source','Disabled By'], int_rows))
    lines.append('')

    lines.append('## Add-on Inventory')
    lines.append('')
    if addons:
        addon_rows = []
        for a in sorted(addons, key=lambda x: x.get('name','')):
            addon_rows.append([
                a.get('name',''), a.get('slug',''), a.get('version',''), a.get('state',''), str(a.get('update_available',False)), a.get('repository','')
            ])
        lines.append(md_table(['Name','Slug','Version','State','Update Available','Repository'], addon_rows))
    else:
        lines.append('_Supervisor add-on inventory was not available from the current token scope at generation time._')
    lines.append('')

    lines.append('## Automation Inventory')
    lines.append('')
    auto_rows = []
    for a in automations:
        attr = a.get('attributes', {})
        auto_rows.append([
            a.get('entity_id',''),
            a.get('state',''),
            attr.get('friendly_name',''),
            attr.get('id',''),
            str(attr.get('last_triggered') or ''),
            attr.get('mode',''),
        ])
    lines.append(md_table(['Entity ID','State','Alias','Automation ID','Last Triggered','Mode'], auto_rows))
    lines.append('')

    lines.append('## NAS Storage Architecture')
    lines.append('')
    lines.append('- NAS host: **Mac Mini** (`192.168.50.208`)')
    lines.append('- SMB share: **`Plex_HD`**')
    lines.append(f'- Local path on this host: `{local_nas_path}`')
    lines.append('')
    lines.append('### Linux automount configuration')
    lines.append('')
    lines.append('`/etc/systemd/system/home-tonmoy-nas.mount`')
    lines.append('```ini')
    lines.append(nas_mount_unit.strip())
    lines.append('```')
    lines.append('')
    lines.append('`/etc/systemd/system/home-tonmoy-nas.automount`')
    lines.append('```ini')
    lines.append(nas_automount_unit.strip())
    lines.append('```')
    lines.append('')
    lines.append('### `/etc/fstab` NAS-related entries')
    lines.append('```fstab')
    for ln in fstab.splitlines():
        if 'Plex_HD' in ln or 'Automount PlexHD' in ln or 'cifs' in ln:
            lines.append(ln)
    lines.append('```')
    lines.append('')
    lines.append('### Folder structure under `Plex_HD` (depth <= 3)')
    lines.append('```text')
    lines.append(nas_tree)
    lines.append('```')
    lines.append('')

    lines.append('## Backup Locations')
    lines.append('')
    lines.append('- Home Assistant local backup store (`.local`)')
    lines.append('- NAS backup folders observed:')
    lines.append(f'  - `{local_nas_path}/Backups/HomeAssistant`')
    lines.append(f'  - `{local_nas_path}/Backups/Home_assistant`')
    lines.append(f'  - `{local_nas_path}/Backups/MacMini`')
    lines.append('')
    if backups:
        b_rows=[]
        for b in sorted(backups, key=lambda x: x.get('date',''), reverse=True):
            b_rows.append([
                b.get('date',''), b.get('slug',''), b.get('name',''), b.get('type',''), b.get('size',''), ','.join([str(x) for x in b.get('locations',[])]), str(b.get('protected',False))
            ])
        lines.append(md_table(['Date','Slug','Name','Type','Size(MB)','Locations','Protected'], b_rows))
    else:
        lines.append('_Backup list not available from current API scope._')
    lines.append('')

    lines.append('## Tailscale Remote Access Architecture')
    lines.append('')
    if ts:
        self_node = ts.get('Self', {})
        lines.append(md_table(['Field','Value'], [
            ['Backend State', ts.get('BackendState','')],
            ['Version', ts.get('Version','')],
            ['This Node', self_node.get('HostName','')],
            ['This Node Tailscale IPs', ', '.join(self_node.get('TailscaleIPs',[]))],
            ['Tailnet', ts.get('CurrentTailnet',{}).get('Name','')],
            ['MagicDNS', ts.get('CurrentTailnet',{}).get('MagicDNSSuffix','')],
        ]))
        # find Mac mini peer route
        peer_rows=[]
        for p in ts.get('Peer', {}).values():
            routes = ', '.join(p.get('PrimaryRoutes',[]) or [])
            peer_rows.append([p.get('HostName',''), p.get('OS',''), ', '.join(p.get('TailscaleIPs',[])), routes, str(p.get('Online',False)), str(p.get('Active',False))])
        lines.append('')
        lines.append(md_table(['Peer Host','OS','Tailscale IPs','Primary Routes','Online','Active'], sorted(peer_rows)))
        lines.append('')
        health = ts.get('Health', [])
        if health:
            lines.append('### Health Warnings')
            for h in health:
                lines.append(f'- {h}')
            lines.append('')
    else:
        lines.append('_Tailscale status was unavailable during generation._')
        lines.append('')

    lines.append('## Failure Scenarios')
    lines.append('')
    lines.append('1. **HA Core unavailable** — automation/control outage on the dedicated Wyse 5070 appliance.')
    lines.append('2. **Mac Mini NAS unavailable** — media + backup share access interrupted, but HA should remain online.')
    lines.append('3. **Tailscale subnet router (Mac Mini) offline** — remote access to LAN/HA interrupted while local HA control should still work.')
    lines.append('4. **Neo blinds hub or local LAN issue** — cover state/control degradation.')
    lines.append('5. **Supervisor add-on failure** (MQTT/Matter/etc.) — integration-specific impact.')
    lines.append('')

    lines.append('## Recovery Procedures')
    lines.append('')
    lines.append('### A) Home Assistant outage')
    lines.append('1. Confirm HA host reachability on `192.168.50.166:8123`.')
    lines.append('2. If host is offline, troubleshoot the Wyse 5070 appliance directly (power, network link, local SSD/boot state).')
    lines.append('3. If host alive but HA down: restart HA Core from supervisor/UI.')
    lines.append('4. If corruption suspected: restore latest healthy backup from HA backup store (no VM snapshot path assumed).')
    lines.append('5. Validate critical integrations: covers, climate, MQTT, mobile app.')
    lines.append('')
    lines.append(f'### B) NAS mount failure (`{local_nas_path}`)')
    lines.append('1. Check Mac Mini reachability: `ping 192.168.50.208`.')
    lines.append('2. On macOS, confirm `/Volumes/Plex_HD` is mounted; on Omarchy, restart automount units:')
    lines.append('   - `sudo systemctl restart home-tonmoy-nas.automount home-tonmoy-nas.mount`')
    lines.append(f'3. Verify mount: `ls {local_nas_path}`.')
    lines.append('4. If auth fails on Omarchy, verify credentials file `/home/tonmoy/.smb/macmini`.')
    lines.append('')
    lines.append('### C) Tailscale remote path failure')
    lines.append('1. On this node: `tailscale status` and check health warnings.')
    lines.append('2. Verify Mac Mini peer is online and advertising route `192.168.50.0/24`.')
    lines.append('3. Restart Tailscale on affected node if needed.')
    lines.append('4. Fall back to local LAN access for emergency operations.')
    lines.append('')
    lines.append('### D) Blinds state desync')
    lines.append('1. Use dashboard **Refresh Blind Status** action (calls `homeassistant.update_entity`).')
    lines.append('2. Prefer Alexa control via HA-exposed entities to preserve state integrity.')
    lines.append('3. Verify cover entities update in Developer Tools → States.')
    lines.append('')

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text('\n'.join(lines) + '\n')
    print(str(OUT_PATH))


if __name__ == '__main__':
    main()
