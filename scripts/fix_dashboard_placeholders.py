from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

p = BASE_DIR / 'ha_config_staging' / 'config' / 'ui' / 'rahmans_command_centre.yaml'
text = p.read_text()

repls = [
    ('id=\"ha-state\">Healthy</div>', 'id=\"ha-state\">--</div>'),
    ('id=\"ha-cpu\">19%</strong>', 'id=\"ha-cpu\">--</strong>'),
    ('id=\"ha-uptime-days\">7d</strong>', 'id=\"ha-uptime-days\">--</strong>'),
    ('id=\"ha-mem\">84%</strong>', 'id=\"ha-mem\">--</strong>'),
    ('id=\"mac-state\">Stable</div>', 'id=\"mac-state\">--</div>'),
    ('id=\"mac-cpu\">65%</strong>', 'id=\"mac-cpu\">--</strong>'),
    ('id=\"mac-disk\">13%</strong>', 'id=\"mac-disk\">--</strong>'),
    ('id=\"mac-ram\">43%</strong>', 'id=\"mac-ram\">--</strong>'),
    ('id=\"om-state\">Connected</div>', 'id=\"om-state\">--</div>'),
    ('id=\"om-cpu\">16%</strong>', 'id=\"om-cpu\">--</strong>'),
    ('id=\"om-disk\">41%</strong>', 'id=\"om-disk\">--</strong>'),
    ('id=\"om-ram\">53%</strong>', 'id=\"om-ram\">--</strong>'),
    ('id=\"net-state\">Online</div>', 'id=\"net-state\">--</div>'),
    ('id=\"net-wan\">Connected</strong>', 'id=\"net-wan\">--</strong>'),
    ('id=\"net-ip\">100.78.195.209</strong>', 'id=\"net-ip\">--</strong>'),
    ('id=\"net-clients\">↓ 0.6\\\n      \\ Mbps / ↑ 0.0 Mbps</strong>', 'id=\"net-clients\">--</strong>'),
    ('style=\"--nas-used:2.0;\"', 'style=\"--nas-used:0;\"'),
    ('id=\"nas-used-text\">2%</div>', 'id=\"nas-used-text\">--</div>'),
    ('id=\"nas-used-percent\">2%</strong>', 'id=\"nas-used-percent\">--</strong>'),
    ('id=\"nas-free-percent\">98%</strong>', 'id=\"nas-free-percent\">--</strong>'),
    ('id=\"nas-media-percent\">80%</strong>', 'id=\"nas-media-percent\">--</strong>'),
    ('id=\"nas-docs-percent\">0%</strong>', 'id=\"nas-docs-percent\">--</strong>'),
    ('id=\"nas-backups-percent\">2%</strong>', 'id=\"nas-backups-percent\">--</strong>'),
    ('id=\"nas-archive-percent\">0%</strong>', 'id=\"nas-archive-percent\">--</strong>'),
]

count = 0
for old, new in repls:
    n = text.count(old)
    if n:
        text = text.replace(old, new)
        count += n

p.write_text(text)
print(f'patched {count} placeholders in {p}')
