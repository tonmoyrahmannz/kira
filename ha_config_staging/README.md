# HA Config Staging: Tuya IR Remote

This folder contains additive Home Assistant config artifacts for the Tuya IR virtual remote implementation.

Target HAOS config root: `/config`

## Staged paths (copy to HA)
- `config/custom_components/tuya_ir_remote/*` -> `/config/custom_components/tuya_ir_remote/*`
- `config/packages/tuya_ir_remote.yaml` -> `/config/packages/tuya_ir_remote.yaml`
- `config/ui/garage_ir_remote.yaml` -> `/config/ui/garage_ir_remote.yaml`
- `config/secrets.tuya_ir_remote.example.yaml` -> reference only

## Required configuration.yaml snippets
```yaml
homeassistant:
  packages: !include_dir_named packages

tuya_ir_remote:
  access_id: !secret tuya_access_id
  access_secret: !secret tuya_access_secret
  endpoint: !secret tuya_endpoint
  infrared_id: ebab7105bb50cd8408etyu
  devices:
    soundbar:
      remote_id: eb63f0598155a83d99dyhf
      remote_index: 414165031
      category_id: 7
    projector:
      remote_id: ebfb979fc0f3bb3f1fjeap
      remote_index: 6667
      category_id: 6

remote:
  - platform: tuya_ir_remote
```

Then restart Home Assistant.

## Add dashboard
Settings -> Dashboards -> Add Dashboard (YAML mode)
- Title: Garage IR Remote
- URL: garage-ir-remote
- YAML file: `ui/garage_ir_remote.yaml`

## Logging (optional)
```yaml
logger:
  logs:
    custom_components.tuya_ir_remote: debug
```
