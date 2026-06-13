# Smart Home Operational Runbook v8

- Generated: 2026-05-16 14:21:07 NZST
- Source snapshot (UTC): 2026-05-15T23:10:18.958253+00:00
- Data sources: Home Assistant REST API, Home Assistant WebSocket registries, Supervisor API (WebSocket), local host NAS state, optional Linux systemd/fstab state, Tailscale status

## System Overview

| Field | Value |
| --- | --- |
| Home Assistant Name | Rahman's Residence |
| HA Version | 2026.4.1 |
| State | RUNNING |
| Config Source | yaml |
| Timezone | Pacific/Auckland |
| Language | en-GB |
| Country | NZ |
| Latitude / Longitude | -41.1292525 / 174.8535063 |
| Components Loaded | 280 |
| Dashboards | 13 |
| Devices (registry) | 96 |
| Entities (state API) | 450 |
| Entities (entity registry) | 617 |
| Automations (entities) | 12 |

## Network Architecture

- Primary LAN inferred from live endpoints and routes: `192.168.50.0/24`
- Home Assistant endpoint in use: `http://homeassistant.local:8123`
- Known key nodes (live + local config):
  - Router/Gateway: `192.168.50.1`
  - Mac Mini NAS/host: `192.168.50.208`
  - HA endpoint used by Kira: `192.168.50.166:8123`
  - Neo Blinds hub (documented): `192.168.50.224:8839`

## Device Registry (all devices)

| Device ID | Name | Area | Manufacturer | Model | Primary Identifier | Disabled |
| --- | --- | --- | --- | --- | --- | --- |
| 7f2139b37683d93ef86e74728671b41e |  Volume DOWN |  | tuya | Tuya Scene | tuya,tysqhbpAh8A4FuV8sfZ |  |
| de667313a8ffc3c610e15cfd31e99ff4 | 1.1.1.1 |  | Ping | None | ping,01KKMS08ZYXKQBC7PQJYJN1AV4 |  |
| 337a027ba504c9f3e76e6d6013cb0422 | 192.168.50.100 |  | Ping | None | ping,01KKNM3693K1QXWTGY2ESW0X4Y |  |
| ff9468a1a349596396ae32080d812094 | 8.8.8.8 |  | Ping | None | ping,01KKNJVYQJGE6B9T9RVBG3VS4C |  |
| 64952aed9a0643b98c6cfaaa4a53d492 | Advanced SSH & Web Terminal |  | Home Assistant Community Apps | Home Assistant App | hassio,a0d7b954_ssh |  |
| 32936a89c07e401cea5646d18e933fe8 | Alexa Media Player |  | alandtse, keatontaylor | integration | hacs,139664351 |  |
| 9d7667f28fc62cc8d6a16c1684a0a1dd | Backup |  | Home Assistant | Home Assistant Backup | backup,backup_manager |  |
| 41cec4acc655315751f1594bd9515832 | Benq projector | Garage | Tuya | Projector (unsupported) | tuya,ebfb979fc0f3bb3f1fjeap |  |
| 18e7bffa27814f550e35fa25591cc7d6 | Better Thermostat UI |  | KartoffelToby | plugin | hacs,439367892 |  |
| 499b1a0446b4e0126f607d0f14474ec7 | Bubble Card |  | Clooos | plugin | hacs,680112919 |  |
| 17f1b27600565c80266fccf4f32c6d3f | Config Template Card |  | iantrich | plugin | hacs,172177543 |  |
| 72b7b4d5fb6d1794f6d0f9ab419204ec | Contact Sensor | Guest Living room | Tuya | Contact Sensor | tuya,eb628a0df1bbfc73da6rff |  |
| b28a1aa677ed391d15c3acbca934531e | Contact Sensor 2 | Master Bedroom | Tuya | Contact Sensor | tuya,eb9884e633e1db834fhtpn |  |
| 090cf0d491e3bee0a7e74667a6f0faeb | Dryer | Garage | LGE | RC90V9_AUS (DEVICE_DRYER) | lg_thinq,b7a4bf36f47c4385f0ec9bf5cf0303c0f6dcac87d5b09913540b9ee16c394acf |  |
| 9bba01d8123cc3818cf976fbb4a1bd06 | Dyson |  | cmgrayb | integration | hacs,1043356454 |  |
| 1cb57f9d286501d415e6a9bca47f2450 | Dyson SZ1-AU-NJA5315A |  | Dyson | 455 | hass_dyson,SZ1-AU-NJA5315A |  |
| c21aa28bbe1785e3b4619e694eb33607 | Esha’s iPhone |  | Apple | iPhone14,3 | mobile_app,65F1C2B1-D4FF-4A82-A3B1-23637CA97C51 |  |
| c00a20fb321d83101668d15dea721951 | Everywhere |  | Amazon | Speaker Group | alexa_media,3970bd0e257c4105ad6bf2b3ee3322f0 |  |
| 27c809895e08af921e0ff095a1303034 | Forecast |  | Met.no | Forecast | met,01KHMGQAYFGE4395ZJW78PR5GJ |  |
| 08d6efd50bb1b7bf4b601cfd1a941af1 | Front Door | Kitching+Living Room+Dining | Ring | Doorbell Elite | ring,047bcb200b1f |  |
| c0d17ad7620607c79c20ee1d877b4a91 | Front Door Live view:21068 |  | Home Assistant | Camera | homekit,01KJW8Z0EVXF4G09M2F5ZJBNTW,homekit.bridge |  |
| 45851fa08a686298bbdd690959ea8a22 | GT-iPhone16-Tonmoy |  | Apple | iPhone17,3 | mobile_app,1ABAB17B-4603-4183-9C0E-34B2E8270460 |  |
| 4abc58f04040d4fc50fd688ad08a5f8f | Garage sensor | Garage | Tuya | zigbee温湿度传感器 | tuya,eb16f28cd9f887da1ehupm |  |
| 9d94c527af1d2b8c20319cd2887dde0f | Google Translate en com |  | Google | Google Translate TTS | google_translate,01KHMGQAY5T1P6YYVXT880XDGE |  |
| 644114405a5fda4206aac52952f0cd61 | Gree A/C |  | robhofmann | integration | hacs,140618233 |  |
| ef735cbfada97bad3bb720ff0583f902 | Guest Bedroom Sensor | Guest Bedroom | Tuya | zigbee温湿度传感器 | tuya,eb3527bce9eed71a81c6ld |  |
| d1ebeb2089e7a2bcd87a2c4e05a07c50 | HACS |  | hacs.xyz |  | hacs,0717a0cd-745c-48fd-9b16-c8534c9704f9-bc944b0f-fd42-4a58-a072-ade38d1444cd |  |
| 0413ab8c8ad65d4cdcdc1d031c9298dc | HASS Bridge 0H:21065 | Kitching+Living Room+Dining | Home Assistant | HomeBridge | homekit,01KJW8Z0EWTXQ0BAQX6R698DQM,homekit.bridge |  |
| a22a10b564c3f67055a32fa16833e24e | HASS Bridge:21064 | Garage | Home Assistant | HomeBridge | homekit,01KJS5PTFP46EQX18SWXJNN750,homekit.bridge |  |
| f2f3929cdf2d00acf9370b9fec00a39b | HP LaserJet M109-M112 | Garage | HP | HP LaserJet M109-M112 | ipp,0ad25a6f-2c50-44e0-808f-7e0ccea3c3fe |  |
| 38e891cbe0bbfc14782f7fc8b1970c88 | Home Assistant Core |  | Home Assistant | Home Assistant Core | hassio,core |  |
| 650599f0d7ecb9ce74b348add2a4be06 | Home Assistant Host |  | Home Assistant | Home Assistant Host | hassio,host |  |
| e01721b13c409a5e69839135694e8dde | Home Assistant Operating System |  | Home Assistant | Home Assistant Operating System | hassio,OS |  |
| 011e3de6bc457a9cce31c216d0f0d1eb | Home Assistant Supervisor |  | Home Assistant | Home Assistant Supervisor | hassio,supervisor |  |
| 440f319327a4b0400a8a8a6fcd7dc42c | Kiosk Mode |  | NemesisRE | plugin | hacs,497319128 |  |
| 0170a804acda758a43e5250bbbd631e1 | Living room |  | Apple | Apple TV 4K (gen 2) | apple_tv,D2:83:E8:A7:AC:9B |  |
| 8c80629af94d96e413ca7b5e82273d4e | Living room sensor | Kitching+Living Room+Dining | Tuya | zigbee温湿度传感器 | tuya,eb64d3edafa0d3defaixkp |  |
| a11ae81cda4fcd36480cbbea9a7f110d | Livingroom Echo | Kitching+Living Room+Dining | Amazon | Echo (Gen2) | alexa_media,G090P301801307LK |  |
| 8236fd986544a15f04dadf191ca530ec | Local Tuya |  | xZetsubou | integration | hacs,653793773 |  |
| f2decf6933767a8ff8e35fc676be8cf3 | Lounge TV | Kitching+Living Room+Dining | Amazon | THIRD_PARTY_AVS_VIDEO_FIRST A11DUJZ8M1DZDE | alexa_media,871ad29552f848b2ab6d8effa072dcc4 |  |
| 4cc5492c7126d4386b6c683156e9d296 | Lovelace Html Card |  | PiotrMachowski | plugin | hacs,193408399 |  |
| 3d9f0e7360bc1439bb21d2abf7b38eab | MacMini |  | Apple | Macmini9,1 | mobile_app,99D02F03-A0BA-5A99-9EC6-A0E954201A57 |  |
| 48f4a819cb987fee163b14ca194f808a | Master Bedroom Sensor | Master Bedroom | Tuya | zigbee温湿度传感器 | tuya,eb5e6b81e490cabde8iuhy |  |
| b492ce0b5e267a94cf33335454ad23c9 | Master bedroom Echo | Master Bedroom | Amazon | Echo Dot (Gen3) | alexa_media,G091B005037203RC |  |
| 4752365e039c0bd0a6e5295c3f68f2fb | Matter Server |  | Official apps | Home Assistant App | hassio,core_matter_server |  |
| 5895c6f67ef318873d5f7bc781c2129c | Minimalistic Area Card |  | junalmeida | plugin | hacs,489457357 |  |
| 2f951ffd6b6cf48a3d2c6bba0b64cd20 | Mushroom |  | piitaya | plugin | hacs,444350375 |  |
| 7685b7cdc7b061c49b0a348f850cb6c8 | Neo Smart Blinds Blue |  | ikifar2012 | integration | hacs,1008725569 |  |
| bb57207c1b9443ed2a2b6c0b6e288baf | Outside | Kitching+Living Room+Dining | Ring | Doorbell Elite | ring,047bcb2008cf |  |
| 28432b9e1f65eaa6cdbe813e408e5b52 | Outside Live view:21067 |  | Home Assistant | Camera | homekit,01KJW8Z0EVF5DTN5VVX5187MMR,homekit.bridge |  |
| 6becd5e1cd0fe305efadb99e47b51184 | PS5-245 |  | Sony | Playstation 5 | mqtt,78C881A814D5 |  |
| 61e72bae18d9355abaa3ad96dd0b65ad | PlayStation 5 | Garage | Sony Interactive Entertainment | PlayStation 5 | playstation_network,1766221986867636538_PS5 |  |
| 66cbf223d1e9593620c6da0ea2880235 | PlayStation 5:21066 |  | Home Assistant | ReceiverMediaPlayer | homekit,01KJW8Z0EP5YWE17VCGC3ZVBQ1,homekit.bridge |  |
| 79e40b46eeeba0c875bc101c25a5da19 | Plex (Plex for Apple TV - Apple TV) |  | tvOS | Plex for Apple TV | plex,017FE60B-22AB-4805-A247-3D37E460E519 |  |
| 2da2afc410114fc3fd6545548e48edb8 | Plex (Plex for PlayStation 5 - PS5-245) |  | PlayStation | Plex for PlayStation 5 | plex,45f0cqa21whdcb4zvfd85l0b |  |
| 5d91aa1e253896222e9f88e9d7823300 | Plex (Plex for iOS - iPad) |  | iOS | Plex for iOS | plex,nhhniqjjd56r1mao5tp5fj89 | user |
| ad6425416ddd5f7e5d981ca5fffcf15b | Plex Client Service |  | Plex | Plex Clients | plex,plex.tv-clients |  |
| 80ab6d604b324983b542aacff1701113 | Plex Meets Home Assistant |  | JurajNyiri | plugin | hacs,363428919 |  |
| 98b3bc3bcedf9ebe4cabdc5a077ffa3d | Projector OFF |  | tuya | Tuya Scene | tuya,tysmW4PGeDlWJDZl1lx |  |
| 3dd18760ef4d81420778e6976995138e | Projector ON |  | tuya | Tuya Scene | tuya,tysA9Oq2BIb7zW3Si3A |  |
| aec6b3240181af5ad522fb1212cc4868 | Projector input |  | tuya | Tuya Scene | tuya,tys4Y4fHj4VR0vyFL6u |  |
| fb43daad4243c6e1bad2a13523cae1b2 | Projector mode |  | tuya | Tuya Scene | tuya,tys4EvU6Y5w49AAX761 |  |
| 1d7f4de704ebd20b1627b8787d93a06d | RT-AX86U-9F68 | Garage | ASUSTeK Computer Inc. | ASUS Wireless Router | upnp_serial_number,M1IFI6002103 |  |
| d0a70869a2eb8d5489a54fddde519f34 | Refrigerator | Kitching+Living Room+Dining | LGE | 2RES1VE61PFD2 (DEVICE_REFRIGERATOR) | lg_thinq,633edd59ad646f6b18779c34bd72b28be314a684fc070188ea1eb5658c2e96dc |  |
| cee4884512c321a8673b4abe7012eaf9 | Samsung The Frame 65 | Kitching+Living Room+Dining | Samsung Electronics | QA65LS03BASXNZ |  |  |
| 18c02378586286e2a84b95a62e456805 | Samsung soundbar | Garage | Tuya | Audio (unsupported) | tuya,eb63f0598155a83d99dyhf |  |
| 19235df7f69ddec5f99ed91591915fbb | Smart IR |  | Tuya | Tuya generic (ebab7105bb50cd8408etyu) | localtuya,local_ebab7105bb50cd8408etyu |  |
| ae32f58e7b7eb3d290866157cc6c5bb1 | Smart IR | Garage | Tuya | Smart IR (unsupported) | tuya,ebab7105bb50cd8408etyu |  |
| f64e4c2cbf7bd8373ca8d02fa9a0bfe1 | Soundbar OFF |  | tuya | Tuya Scene | tuya,tys5btsID90ISWeIImy |  |
| b5ad89967671400df3c74411fad5eb49 | Soundbar ON | Garage | tuya | Tuya Scene | tuya,tyswMSAdcO1IqSdPC4V |  |
| 50dab0dda1ae943b6899907e3f736d39 | Soundbar bluetooth |  | tuya | Tuya Scene | tuya,tysw8M5ILevRmixnJ60 |  |
| fdad0809ca11ca6447f4f58bdf297e3d | Study Echo | Study | Amazon | Echo Dot (Gen4) | alexa_media,G091AA13212309B6 |  |
| defedd9c7cc79a84a378eb002606088d | Study sensor | Study | Tuya | zigbee温湿度传感器 | tuya,ebac3c4adb361e88f69l6h |  |
| 46c2ac25e3ed4d8b02630bd625ffe6bd | Sun |  | None | None | sun,01KHMEG49ATMWG6P48E5SGCE9Q |  |
| a2682f234290d78a1f6e912b9468ead5 | System Monitor |  | System Monitor | None | systemmonitor,01KKMRZBGWREKMBJ9898KBJY9W |  |
| 2707e067fe901832bf908d4deb1cb9ca | This Device |  | Amazon | Alexa Mobile Voice iOS | alexa_media,a4741b7ce895e6b6eb737a7807179079 |  |
| 03904f513f0045a6baf94eb09be9c066 | Tonmoy's Sony WH-1000XM3 |  | Amazon | UNKNOWN A3GZUE7F9MEB4U | alexa_media,ceb6bf1f8ce844b49a760c6f42a84685 |  |
| 9418289693162d7abc44504ae08712e0 | Tonmoy's iPad |  | Apple | iPad4,1 | mobile_app,B7DDF46D-DE88-492E-B1E4-C2AEE26705D8 |  |
| 134c03a7908c30788d042f4c6d9d18c9 | TonmoysPlexServer | Kitching+Living Room+Dining | Plex | Plex Media Server | plex,d2efa7e26e73b9cc690a50b17f3c358a92f84ccd |  |
| 3d2cb4976086163eb018489745b7e31c | Upcoming Media Card |  | custom-cards | plugin | hacs,146783593 |  |
| 77985371d7d77ed8cfd4ebe25de42fc6 | Volume UP |  | tuya | Tuya Scene | tuya,tysGioqV13rcA0ckPqJ |  |
| bb38c4bd14ab0724a436eaa871ba8ddb | Washing machine | Garage | LGE | F_V8_Y___W.B__QEUK (DEVICE_WASHER) | lg_thinq,f87fca3aa060ee436427dad21511c70ed904c49c5aafa3467a13d6ae3cd2d2ad |  |
| 6feb2d023c3351e2ce1001764cace3bb | Wi-Fi Power Strip | Garage | Tuya | Wi-Fi Power Strip | tuya,eb7c2f768824d3fdfcxxuq |  |
| 6eff8a2cd6ad829df49dcd9ee34cd877 | Zigbee LAN Gateway | Garage | Tuya | Zigbee LAN Gateway (unsupported) | tuya,eb67aa1ba56b7739f8eqla |  |
| d6440512f7f28cf2bc3760a1b2c1d5cc | apexcharts-card |  | RomRider | plugin | hacs,331701152 |  |
| 6567fd4c7c68fdd6056af0441be573fd | auto-entities |  | thomasloven | plugin | hacs,167744584 |  |
| 6889e9f30bab3c7f0ac95d8236c4e214 | button-card |  | custom-cards | plugin | hacs,146194325 |  |
| 5cf8923f4cd057685c005c91f5bb2e2f | card-mod |  | thomasloven | plugin | hacs,190927524 |  |
| d0cfef5a0879baee353afc244a34d1b5 | expander-card |  | MelleD | plugin | hacs,677140532 |  |
| e0864a04a875f40f6063e5cad6205072 | gateway S | Garage | Tuya | gateway S (unsupported) | tuya,ebf172f077ec7b1cc6bz7w |  |
| d0b2dd240afae10e7c54df7366c1bccf | ha-floorplan 🖌🎨 \| Your imagination (almost) defines the limits |  | ExperienceLovelace | plugin | hacs,188323494 |  |
| 4cbbd019c1c324f2830af3835a14573c | iPad (2) |  | Apple | iPad4,1 | mobile_app,E58ABB96-3604-4C1A-8395-25E588B0692D |  |
| d31cb9e882ea36545f8699e5dc9ed198 | layout-card |  | thomasloven | plugin | hacs,156434866 |  |
| a98e7eab77d8f445afa3ae8253abd65e | mini-graph-card |  | kalkih | plugin | hacs,151280062 |  |
| 6295e8c914d5670c237ba9834b284d28 | plex_hd_backups_homeassistant |  | Home Assistant | Home Assistant Mount | hassio,mount_plex_hd_backups_homeassistant |  |
| d5d74eea9b41c73198534d7dd8c4ddc6 | tonmoyNZ | Garage | Sony Interactive Entertainment | None | playstation_network,1766221986867636538 |  |

## Entity Inventory (all entities)

### Entity Domain Summary (entity registry)

| Domain | Count |
| --- | --- |
| automation | 12 |
| binary_sensor | 43 |
| button | 2 |
| calendar | 2 |
| camera | 3 |
| climate | 6 |
| cover | 6 |
| device_tracker | 8 |
| event | 10 |
| fan | 1 |
| image | 3 |
| input_datetime | 1 |
| input_number | 1 |
| media_player | 15 |
| notify | 12 |
| number | 7 |
| person | 4 |
| remote | 4 |
| scene | 9 |
| script | 29 |
| select | 4 |
| sensor | 340 |
| switch | 62 |
| todo | 1 |
| tts | 1 |
| update | 30 |
| weather | 1 |

| Entity ID | State | Platform | Device ID | Area | Disabled By | Hidden By |
| --- | --- | --- | --- | --- | --- | --- |
| automation.alexa_sync_dining_blind_1 | off | automation | None |  |  |  |
| automation.alexa_sync_dining_blind_2 | off | automation | None |  |  |  |
| automation.alexa_sync_living_room_blind | off | automation | None |  |  |  |
| automation.alexa_sync_master_bedroom_blind | off | automation | None |  |  |  |
| automation.alexa_sync_sophie_s_blind | off | automation | None |  |  |  |
| automation.alexa_sync_study_blind | off | automation | None |  |  |  |
| automation.auto_start_heater | on | automation | None |  |  |  |
| automation.mealprep_refresh_today_s_meal_every_15_min | unavailable | automation | None |  |  |  |
| automation.mealprep_refresh_today_s_meal_on_ha_start | unavailable | automation | None |  |  |  |
| automation.new_automation | on | automation | None |  |  |  |
| automation.openclaw_self_recovery | on | automation | None |  |  |  |
| automation.set_ac_fan_speed_from_slider | on | automation | None |  |  |  |
| binary_sensor.192_168_50_100 | on | ping | 337a027ba504c9f3e76e6d6013cb0422 |  |  |  |
| binary_sensor.1_1_1_1 | on | ping | de667313a8ffc3c610e15cfd31e99ff4 |  |  |  |
| binary_sensor.8_8_8_8 | on | ping | ff9468a1a349596396ae32080d812094 |  |  |  |
| binary_sensor.advanced_ssh_web_terminal_running | unavailable_in_state_api | hassio | 64952aed9a0643b98c6cfaaa4a53d492 |  | integration |  |
| binary_sensor.contact_sensor_2_door | off | tuya | b28a1aa677ed391d15c3acbca934531e |  |  |  |
| binary_sensor.contact_sensor_2_tamper | off | tuya | b28a1aa677ed391d15c3acbca934531e |  |  |  |
| binary_sensor.contact_sensor_door | on | tuya | 72b7b4d5fb6d1794f6d0f9ab419204ec |  |  |  |
| binary_sensor.contact_sensor_tamper | off | tuya | 72b7b4d5fb6d1794f6d0f9ab419204ec |  |  |  |
| binary_sensor.dryer_remote_start | off | lg_thinq | 090cf0d491e3bee0a7e74667a6f0faeb |  |  |  |
| binary_sensor.dyson_sz1_au_nja5315a_fault_motor | off | hass_dyson | 1cb57f9d286501d415e6a9bca47f2450 |  |  |  |
| binary_sensor.dyson_sz1_au_nja5315a_fault_power_supply | off | hass_dyson | 1cb57f9d286501d415e6a9bca47f2450 |  |  |  |
| binary_sensor.dyson_sz1_au_nja5315a_fault_system | off | hass_dyson | 1cb57f9d286501d415e6a9bca47f2450 |  |  |  |
| binary_sensor.dyson_sz1_au_nja5315a_fault_temperature_sensor | off | hass_dyson | 1cb57f9d286501d415e6a9bca47f2450 |  |  |  |
| binary_sensor.dyson_sz1_au_nja5315a_fault_wifi_connection | off | hass_dyson | 1cb57f9d286501d415e6a9bca47f2450 |  |  |  |
| binary_sensor.dyson_sz1_au_nja5315a_filter_replacement | off | hass_dyson | 1cb57f9d286501d415e6a9bca47f2450 |  |  |  |
| binary_sensor.kira_online | unavailable | template | None |  |  |  |
| binary_sensor.kira_openclaw_running | unavailable | template | None |  |  |  |
| binary_sensor.macmini_active | unavailable | mobile_app | 3d9f0e7360bc1439bb21d2abf7b38eab |  |  |  |
| binary_sensor.macmini_audio_input_in_use | unavailable | mobile_app | 3d9f0e7360bc1439bb21d2abf7b38eab |  |  |  |
| binary_sensor.macmini_audio_output_in_use | unavailable | mobile_app | 3d9f0e7360bc1439bb21d2abf7b38eab |  |  |  |
| binary_sensor.macmini_camera_in_use | unavailable | mobile_app | 3d9f0e7360bc1439bb21d2abf7b38eab |  |  |  |
| binary_sensor.matter_server_running | unavailable_in_state_api | hassio | 4752365e039c0bd0a6e5295c3f68f2fb |  | integration |  |
| binary_sensor.mqtt_service_online | off | command_line | None |  |  |  |
| binary_sensor.nas_online | on | command_line | None |  |  |  |
| binary_sensor.omarchy_online | unavailable | template | None |  |  |  |
| binary_sensor.omarchy_tailscale_connected | unavailable | template | None |  |  |  |
| binary_sensor.openclaw_service_online | off | template | None |  |  |  |
| binary_sensor.ping_cloudflare | on | template | None |  |  |  |
| binary_sensor.ping_google | on | template | None |  |  |  |
| binary_sensor.plex_hd_backups_homeassistant_connected | unavailable_in_state_api | hassio | 6295e8c914d5670c237ba9834b284d28 |  | integration |  |
| binary_sensor.plex_service_online | on | command_line | None |  |  |  |
| binary_sensor.refrigerator_door | off | lg_thinq | d0a70869a2eb8d5489a54fddde519f34 |  |  |  |
| binary_sensor.rt_ax86u_9f68_wan_status | on | upnp | 1d7f4de704ebd20b1627b8787d93a06d |  |  |  |
| binary_sensor.sun_solar_rising | unavailable_in_state_api | sun | 46c2ac25e3ed4d8b02630bd625ffe6bd |  | integration |  |
| binary_sensor.system_monitor_charging | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| binary_sensor.tailscale_any_device_offline | off | template | None |  |  |  |
| binary_sensor.tailscale_esha_iphone_online | on | template | None |  |  |  |
| binary_sensor.tailscale_service_online | off | template | None |  |  |  |
| binary_sensor.tailscale_tailnet_healthy | on | template | None |  |  |  |
| binary_sensor.tailscale_tonmoy_iphone_online | on | template | None |  |  |  |
| binary_sensor.tonmoynz_subscribed_to_playstation_plus | unavailable | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  |  |  |
| binary_sensor.washing_machine_remote_start | off | lg_thinq | bb38c4bd14ab0724a436eaa871ba8ddb |  |  |  |
| binary_sensor.zigbee_service_online | on | template | None |  |  |  |
| button.dyson_sz1_au_nja5315a_reconnect | unknown | hass_dyson | 1cb57f9d286501d415e6a9bca47f2450 |  |  |  |
| button.tonmoysplexserver_scan_clients | unknown | plex | 134c03a7908c30788d042f4c6d9d18c9 |  |  |  |
| calendar.airbnb | on | remote_calendar | None |  |  |  |
| calendar.booking_com | off | remote_calendar | None |  |  |  |
| camera.front_door_live_view | idle | ring | 08d6efd50bb1b7bf4b601cfd1a941af1 |  |  |  |
| camera.outside_last_recording | unavailable_in_state_api | ring | bb57207c1b9443ed2a2b6c0b6e288baf |  | integration |  |
| camera.outside_live_view | idle | ring | bb57207c1b9443ed2a2b6c0b6e288baf |  |  |  |
| climate.ac_bedroom | auto | gree | None |  |  |  |
| climate.ac_guest_room | auto | gree | None |  |  |  |
| climate.ac_living_room | auto | gree | None |  |  |  |
| climate.ac_master | off | gree | None |  |  |  |
| climate.ac_study | auto | gree | None |  |  |  |
| climate.dyson_sz1_au_nja5315a | heat | hass_dyson | 1cb57f9d286501d415e6a9bca47f2450 |  |  |  |
| cover.dining_blind_1 | open | neosmartblinds | None |  |  |  |
| cover.dining_blind_2_3 | open | neosmartblinds | None | Kitching+Living Room+Dining |  |  |
| cover.living_room_blind | open | neosmartblinds | None |  |  |  |
| cover.master_bedroom_blind | open | neosmartblinds | None |  |  |  |
| cover.sophie_s_blind | open | neosmartblinds | None |  |  |  |
| cover.study_blind | open | neosmartblinds | None |  |  |  |
| device_tracker.192_168_50_100 | unavailable_in_state_api | ping | 337a027ba504c9f3e76e6d6013cb0422 |  | integration |  |
| device_tracker.1_1_1_1 | unavailable_in_state_api | ping | de667313a8ffc3c610e15cfd31e99ff4 |  | integration |  |
| device_tracker.8_8_8_8 | unavailable_in_state_api | ping | ff9468a1a349596396ae32080d812094 |  | integration |  |
| device_tracker.eshas_iphone | home | mobile_app | c21aa28bbe1785e3b4619e694eb33607 |  |  |  |
| device_tracker.gt_iphone16_tonmoy | home | mobile_app | 45851fa08a686298bbdd690959ea8a22 |  |  |  |
| device_tracker.ipad | home | mobile_app | 4cbbd019c1c324f2830af3835a14573c |  |  |  |
| device_tracker.macmini | home | mobile_app | 3d9f0e7360bc1439bb21d2abf7b38eab |  |  |  |
| device_tracker.tonmoy_s_ipad | home | mobile_app | 9418289693162d7abc44504ae08712e0 |  |  |  |
| event.backup_automatic_backup | 2026-05-15T17:11:28.233+00:00 | backup | 9d7667f28fc62cc8d6a16c1684a0a1dd |  |  |  |
| event.dryer_error | unknown | lg_thinq | 090cf0d491e3bee0a7e74667a6f0faeb |  |  |  |
| event.dryer_notification | 2026-03-16T14:34:08.031+00:00 | lg_thinq | 090cf0d491e3bee0a7e74667a6f0faeb |  |  |  |
| event.front_door_ding | unknown | ring | 08d6efd50bb1b7bf4b601cfd1a941af1 |  |  |  |
| event.front_door_motion | unknown | ring | 08d6efd50bb1b7bf4b601cfd1a941af1 |  |  |  |
| event.outside_ding | 2026-04-18T07:04:56.388+00:00 | ring | bb57207c1b9443ed2a2b6c0b6e288baf |  |  |  |
| event.outside_motion | 2026-05-15T23:07:45.291+00:00 | ring | bb57207c1b9443ed2a2b6c0b6e288baf |  |  |  |
| event.refrigerator_notification | 2026-05-09T03:36:49.963+00:00 | lg_thinq | d0a70869a2eb8d5489a54fddde519f34 |  |  |  |
| event.washing_machine_error | unknown | lg_thinq | bb38c4bd14ab0724a436eaa871ba8ddb |  |  |  |
| event.washing_machine_notification | 2026-05-15T21:47:17.473+00:00 | lg_thinq | bb38c4bd14ab0724a436eaa871ba8ddb |  |  |  |
| fan.dyson_sz1_au_nja5315a | on | hass_dyson | 1cb57f9d286501d415e6a9bca47f2450 |  |  |  |
| image.tonmoynz_avatar | unavailable | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  |  |  |
| image.tonmoynz_now_playing | unavailable | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  |  |  |
| image.tonmoynz_share_profile | unavailable | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  |  |  |
| input_datetime.openclaw_last_auto_recovery | 2026-05-09 10:59:52 | input_datetime | None |  |  |  |
| input_number.ac_fan_speed_level | 4.0 | input_number | None |  |  |  |
| media_player.everywhere | unavailable | alexa_media | c00a20fb321d83101668d15dea721951 |  |  |  |
| media_player.living_room | off | apple_tv | 0170a804acda758a43e5250bbbd631e1 |  |  |  |
| media_player.livingroom_echo | unavailable | alexa_media | a11ae81cda4fcd36480cbbea9a7f110d |  |  |  |
| media_player.lounge_tv | unavailable | alexa_media | f2decf6933767a8ff8e35fc676be8cf3 |  |  |  |
| media_player.master_bedroom_echo | unavailable | alexa_media | b492ce0b5e267a94cf33335454ad23c9 |  |  |  |
| media_player.playstation_5 | unavailable | playstation_network | 61e72bae18d9355abaa3ad96dd0b65ad |  |  |  |
| media_player.plex_plex_for_apple_tv_apple_tv | unavailable | plex | 79e40b46eeeba0c875bc101c25a5da19 |  |  |  |
| media_player.plex_plex_for_ios_ipad | unavailable_in_state_api | plex | 5d91aa1e253896222e9f88e9d7823300 |  | device |  |
| media_player.plex_plex_for_playstation_5_ps5_245 | unavailable | plex | 2da2afc410114fc3fd6545548e48edb8 |  |  |  |
| media_player.plex_plex_web_chrome_linux | unavailable | plex | ad6425416ddd5f7e5d981ca5fffcf15b |  |  |  |
| media_player.plex_plex_web_chrome_osx | unavailable | plex | ad6425416ddd5f7e5d981ca5fffcf15b |  |  |  |
| media_player.samsung_the_frame_65 | idle | dlna_dmr | cee4884512c321a8673b4abe7012eaf9 |  |  |  |
| media_player.study_echo | unavailable | alexa_media | fdad0809ca11ca6447f4f58bdf297e3d |  |  |  |
| media_player.this_device_2 | idle | alexa_media | 2707e067fe901832bf908d4deb1cb9ca |  |  |  |
| media_player.tonmoy_s_sony_wh_1000xm3 | unavailable | alexa_media | 03904f513f0045a6baf94eb09be9c066 |  |  |  |
| notify.tonmoynz_direct_message_cyber_alien007 | unavailable_in_state_api | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  | integration |  |
| notify.tonmoynz_direct_message_erlyme | unavailable_in_state_api | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  | integration |  |
| notify.tonmoynz_direct_message_icknay | unavailable_in_state_api | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  | integration |  |
| notify.tonmoynz_direct_message_ishtiopal | unavailable_in_state_api | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  | integration |  |
| notify.tonmoynz_direct_message_khamas3 | unavailable_in_state_api | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  | integration |  |
| notify.tonmoynz_direct_message_krisruthless | unavailable_in_state_api | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  | integration |  |
| notify.tonmoynz_direct_message_smoooveheadshot | unavailable_in_state_api | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  | integration |  |
| notify.tonmoynz_direct_message_symbolic4real | unavailable_in_state_api | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  | integration |  |
| notify.tonmoynz_direct_message_trikaal | unavailable_in_state_api | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  | integration |  |
| notify.tonmoynz_direct_message_vihunz07 | unavailable_in_state_api | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  | integration |  |
| notify.tonmoynz_group_dhamakka_gamer_gang | unavailable | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  |  |  |
| notify.tonmoynz_group_kupi98_u_sufunny | unavailable | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  |  |  |
| number.dryer_delayed_end | 0 | lg_thinq | 090cf0d491e3bee0a7e74667a6f0faeb |  |  |  |
| number.dyson_sz1_au_nja5315a_sleep_timer | 0 | hass_dyson | 1cb57f9d286501d415e6a9bca47f2450 |  |  |  |
| number.front_door_volume | 11.0 | ring | 08d6efd50bb1b7bf4b601cfd1a941af1 |  |  |  |
| number.outside_volume | 10.0 | ring | bb57207c1b9443ed2a2b6c0b6e288baf |  |  |  |
| number.refrigerator_freezer_temperature | -18 | lg_thinq | d0a70869a2eb8d5489a54fddde519f34 |  |  |  |
| number.refrigerator_fridge_temperature | 3 | lg_thinq | d0a70869a2eb8d5489a54fddde519f34 |  |  |  |
| number.washing_machine_delayed_end | 0 | lg_thinq | bb38c4bd14ab0724a436eaa871ba8ddb |  |  |  |
| person.esha | home | person | None |  |  |  |
| person.homeassistant_docker | home | person | None |  |  |  |
| person.ipad_old | home | person | None |  |  |  |
| person.macmini | unknown | person | None |  |  |  |
| remote.living_room | on | apple_tv | 0170a804acda758a43e5250bbbd631e1 |  |  |  |
| remote.projector_ir_remote | on | tuya_ir_remote | None |  |  |  |
| remote.smart_ir_garage_ir_remote | unavailable | localtuya | 19235df7f69ddec5f99ed91591915fbb |  |  |  |
| remote.soundbar_ir_remote | on | tuya_ir_remote | None |  |  |  |
| scene.projector_input | 2026-03-09T00:56:50.592260+00:00 | tuya | aec6b3240181af5ad522fb1212cc4868 |  |  |  |
| scene.projector_mode | 2026-04-12T03:56:44.585119+00:00 | tuya | fb43daad4243c6e1bad2a13523cae1b2 |  |  |  |
| scene.projector_off | 2026-03-06T13:18:24.422153+00:00 | tuya | 98b3bc3bcedf9ebe4cabdc5a077ffa3d |  |  |  |
| scene.projector_on | 2026-03-22T07:00:07.833153+00:00 | tuya | 3dd18760ef4d81420778e6976995138e |  |  |  |
| scene.soundbar_bluetooth | 2026-03-09T00:57:06.229306+00:00 | tuya | 50dab0dda1ae943b6899907e3f736d39 |  |  |  |
| scene.soundbar_off | 2026-03-04T05:30:42.616712+00:00 | tuya | f64e4c2cbf7bd8373ca8d02fa9a0bfe1 |  |  |  |
| scene.soundbar_on | 2026-03-09T00:56:57.459774+00:00 | tuya | b5ad89967671400df3c74411fad5eb49 |  |  |  |
| scene.volume_down | 2026-03-09T00:02:17.776597+00:00 | tuya | 7f2139b37683d93ef86e74728671b41e |  |  |  |
| scene.volume_up | 2026-03-09T00:02:20.110561+00:00 | tuya | 77985371d7d77ed8cfd4ebe25de42fc6 |  |  |  |
| script.cool_all_zones | off | script | None |  |  |  |
| script.heat_all_zones | off | script | None |  |  |  |
| script.projector_back | off | script | None |  |  |  |
| script.projector_down | off | script | None |  |  |  |
| script.projector_exit | off | script | None |  |  |  |
| script.projector_info | off | script | None |  |  |  |
| script.projector_input | off | script | None |  |  |  |
| script.projector_left | off | script | None |  |  |  |
| script.projector_menu | off | script | None |  |  |  |
| script.projector_mode | off | script | None |  |  |  |
| script.projector_mute | off | script | None |  |  |  |
| script.projector_ok | off | script | None |  |  |  |
| script.projector_power_off | off | script | None |  |  |  |
| script.projector_power_on | off | script | None |  |  |  |
| script.projector_right | off | script | None |  |  |  |
| script.projector_source | off | script | None |  |  |  |
| script.projector_up | off | script | None |  |  |  |
| script.set_all_zones_20c | off | script | None |  |  |  |
| script.set_all_zones_22c | off | script | None |  |  |  |
| script.soundbar_bluetooth | off | script | None |  |  |  |
| script.soundbar_next | off | script | None |  |  |  |
| script.soundbar_pause | off | script | None |  |  |  |
| script.soundbar_play | off | script | None |  |  |  |
| script.soundbar_power | off | script | None |  |  |  |
| script.soundbar_previous | off | script | None |  |  |  |
| script.soundbar_volume_down | off | script | None |  |  |  |
| script.soundbar_volume_up | off | script | None |  |  |  |
| script.turn_off_all_zones | off | script | None |  |  |  |
| script.turn_on_all_zones | off | script | None |  |  |  |
| select.dryer_operation | unknown | lg_thinq | 090cf0d491e3bee0a7e74667a6f0faeb |  |  |  |
| select.washing_machine_operation | unknown | lg_thinq | bb38c4bd14ab0724a436eaa871ba8ddb |  |  |  |
| select.wi_fi_power_strip_indicator_light_mode | unavailable | tuya | 6feb2d023c3351e2ce1001764cace3bb |  |  |  |
| select.wi_fi_power_strip_power_on_behaviour | unavailable | tuya | 6feb2d023c3351e2ce1001764cace3bb |  |  |  |
| sensor.192_168_50_100_jitter | unavailable_in_state_api | ping | 337a027ba504c9f3e76e6d6013cb0422 |  | integration |  |
| sensor.192_168_50_100_packet_loss | unavailable_in_state_api | ping | 337a027ba504c9f3e76e6d6013cb0422 |  | integration |  |
| sensor.192_168_50_100_round_trip_time_average | unavailable_in_state_api | ping | 337a027ba504c9f3e76e6d6013cb0422 |  | integration |  |
| sensor.192_168_50_100_round_trip_time_maximum | unavailable_in_state_api | ping | 337a027ba504c9f3e76e6d6013cb0422 |  | integration |  |
| sensor.192_168_50_100_round_trip_time_minimum | unavailable_in_state_api | ping | 337a027ba504c9f3e76e6d6013cb0422 |  | integration |  |
| sensor.1_1_1_1_jitter | unavailable_in_state_api | ping | de667313a8ffc3c610e15cfd31e99ff4 |  | integration |  |
| sensor.1_1_1_1_packet_loss | unavailable_in_state_api | ping | de667313a8ffc3c610e15cfd31e99ff4 |  | integration |  |
| sensor.1_1_1_1_round_trip_time_average | unavailable_in_state_api | ping | de667313a8ffc3c610e15cfd31e99ff4 |  | integration |  |
| sensor.1_1_1_1_round_trip_time_maximum | unavailable_in_state_api | ping | de667313a8ffc3c610e15cfd31e99ff4 |  | integration |  |
| sensor.1_1_1_1_round_trip_time_minimum | unavailable_in_state_api | ping | de667313a8ffc3c610e15cfd31e99ff4 |  | integration |  |
| sensor.8_8_8_8_jitter | unavailable_in_state_api | ping | ff9468a1a349596396ae32080d812094 |  | integration |  |
| sensor.8_8_8_8_packet_loss | unavailable_in_state_api | ping | ff9468a1a349596396ae32080d812094 |  | integration |  |
| sensor.8_8_8_8_round_trip_time_average | unavailable_in_state_api | ping | ff9468a1a349596396ae32080d812094 |  | integration |  |
| sensor.8_8_8_8_round_trip_time_maximum | unavailable_in_state_api | ping | ff9468a1a349596396ae32080d812094 |  | integration |  |
| sensor.8_8_8_8_round_trip_time_minimum | unavailable_in_state_api | ping | ff9468a1a349596396ae32080d812094 |  | integration |  |
| sensor.ac_fan_speed | Low | template | None |  |  |  |
| sensor.advanced_ssh_web_terminal_cpu_percent | unavailable_in_state_api | hassio | 64952aed9a0643b98c6cfaaa4a53d492 |  | integration |  |
| sensor.advanced_ssh_web_terminal_memory_percent | unavailable_in_state_api | hassio | 64952aed9a0643b98c6cfaaa4a53d492 |  | integration |  |
| sensor.advanced_ssh_web_terminal_newest_version | unavailable_in_state_api | hassio | 64952aed9a0643b98c6cfaaa4a53d492 |  | integration |  |
| sensor.advanced_ssh_web_terminal_version | unavailable_in_state_api | hassio | 64952aed9a0643b98c6cfaaa4a53d492 |  | integration |  |
| sensor.backup_backup_manager_state | idle | backup | 9d7667f28fc62cc8d6a16c1684a0a1dd |  |  |  |
| sensor.backup_last_attempted_automatic_backup | 2026-05-15T17:11:21+00:00 | backup | 9d7667f28fc62cc8d6a16c1684a0a1dd |  |  |  |
| sensor.backup_last_successful_automatic_backup | 2026-05-15T17:11:28+00:00 | backup | 9d7667f28fc62cc8d6a16c1684a0a1dd |  |  |  |
| sensor.backup_next_scheduled_automatic_backup | 2026-05-16T17:12:35+00:00 | backup | 9d7667f28fc62cc8d6a16c1684a0a1dd |  |  |  |
| sensor.contact_sensor_2_battery | 100.0 | tuya | b28a1aa677ed391d15c3acbca934531e |  |  |  |
| sensor.contact_sensor_battery | 100.0 | tuya | 72b7b4d5fb6d1794f6d0f9ab419204ec |  |  |  |
| sensor.dryer_current_status | power_off | lg_thinq | 090cf0d491e3bee0a7e74667a6f0faeb |  |  |  |
| sensor.dryer_delayed_end | unknown | lg_thinq | 090cf0d491e3bee0a7e74667a6f0faeb |  |  |  |
| sensor.dryer_remaining_time | unknown | lg_thinq | 090cf0d491e3bee0a7e74667a6f0faeb |  |  |  |
| sensor.dryer_total_time | unknown | lg_thinq | 090cf0d491e3bee0a7e74667a6f0faeb |  |  |  |
| sensor.dyson_sz1_au_nja5315a_air_quality_category | Good | hass_dyson | 1cb57f9d286501d415e6a9bca47f2450 |  |  |  |
| sensor.dyson_sz1_au_nja5315a_air_quality_index | 6 | hass_dyson | 1cb57f9d286501d415e6a9bca47f2450 |  |  |  |
| sensor.dyson_sz1_au_nja5315a_connection_status | Local | hass_dyson | 1cb57f9d286501d415e6a9bca47f2450 |  |  |  |
| sensor.dyson_sz1_au_nja5315a_dominant_pollutant | PM2.5 | hass_dyson | 1cb57f9d286501d415e6a9bca47f2450 |  |  |  |
| sensor.dyson_sz1_au_nja5315a_hepa_filter_life | 0 | hass_dyson | 1cb57f9d286501d415e6a9bca47f2450 |  |  |  |
| sensor.dyson_sz1_au_nja5315a_hepa_filter_type | Not Installed | hass_dyson | 1cb57f9d286501d415e6a9bca47f2450 |  |  |  |
| sensor.dyson_sz1_au_nja5315a_humidity | 52 | hass_dyson | 1cb57f9d286501d415e6a9bca47f2450 |  |  |  |
| sensor.dyson_sz1_au_nja5315a_particulates | 4 | hass_dyson | 1cb57f9d286501d415e6a9bca47f2450 |  |  |  |
| sensor.dyson_sz1_au_nja5315a_temperature | 20.7 | hass_dyson | 1cb57f9d286501d415e6a9bca47f2450 |  |  |  |
| sensor.dyson_sz1_au_nja5315a_voc | 0.001 | hass_dyson | 1cb57f9d286501d415e6a9bca47f2450 |  |  |  |
| sensor.dyson_sz1_au_nja5315a_wifi_signal | -34 | hass_dyson | 1cb57f9d286501d415e6a9bca47f2450 |  |  |  |
| sensor.eshas_iphone_app_version | 2026.2.1 | mobile_app | c21aa28bbe1785e3b4619e694eb33607 |  |  |  |
| sensor.eshas_iphone_audio_output | unavailable | mobile_app | c21aa28bbe1785e3b4619e694eb33607 |  |  |  |
| sensor.eshas_iphone_battery_level | 25 | mobile_app | c21aa28bbe1785e3b4619e694eb33607 |  |  |  |
| sensor.eshas_iphone_battery_state | Not Charging | mobile_app | c21aa28bbe1785e3b4619e694eb33607 |  |  |  |
| sensor.eshas_iphone_bssid | unavailable | mobile_app | c21aa28bbe1785e3b4619e694eb33607 |  |  |  |
| sensor.eshas_iphone_connection_type | unavailable | mobile_app | c21aa28bbe1785e3b4619e694eb33607 |  |  |  |
| sensor.eshas_iphone_geocoded_location | unavailable | mobile_app | c21aa28bbe1785e3b4619e694eb33607 |  |  |  |
| sensor.eshas_iphone_last_update_trigger | unavailable | mobile_app | c21aa28bbe1785e3b4619e694eb33607 |  |  |  |
| sensor.eshas_iphone_location_permission | Authorized when in use | mobile_app | c21aa28bbe1785e3b4619e694eb33607 |  |  |  |
| sensor.eshas_iphone_sim_1 | unavailable | mobile_app | c21aa28bbe1785e3b4619e694eb33607 |  |  |  |
| sensor.eshas_iphone_sim_2 | unavailable | mobile_app | c21aa28bbe1785e3b4619e694eb33607 |  |  |  |
| sensor.eshas_iphone_ssid | unavailable | mobile_app | c21aa28bbe1785e3b4619e694eb33607 |  |  |  |
| sensor.eshas_iphone_storage | unavailable | mobile_app | c21aa28bbe1785e3b4619e694eb33607 |  |  |  |
| sensor.front_door_battery | unknown | ring | 08d6efd50bb1b7bf4b601cfd1a941af1 |  |  |  |
| sensor.front_door_last_activity | 2026-05-04T15:01:50+00:00 | ring | 08d6efd50bb1b7bf4b601cfd1a941af1 |  |  |  |
| sensor.front_door_signal_strength | unavailable_in_state_api | ring | 08d6efd50bb1b7bf4b601cfd1a941af1 |  | integration |  |
| sensor.front_door_wi_fi_signal_category | unavailable_in_state_api | ring | 08d6efd50bb1b7bf4b601cfd1a941af1 |  | integration |  |
| sensor.garage_sensor_battery | 97.0 | tuya | 4abc58f04040d4fc50fd688ad08a5f8f |  |  |  |
| sensor.garage_sensor_humidity | 51.0 | tuya | 4abc58f04040d4fc50fd688ad08a5f8f |  |  |  |
| sensor.garage_sensor_temperature | 21.4 | tuya | 4abc58f04040d4fc50fd688ad08a5f8f |  |  |  |
| sensor.gt_iphone16_tonmoy_app_version | 2026.4.1 | mobile_app | 45851fa08a686298bbdd690959ea8a22 |  |  |  |
| sensor.gt_iphone16_tonmoy_audio_output | unavailable | mobile_app | 45851fa08a686298bbdd690959ea8a22 |  |  |  |
| sensor.gt_iphone16_tonmoy_battery_level | 100 | mobile_app | 45851fa08a686298bbdd690959ea8a22 |  |  |  |
| sensor.gt_iphone16_tonmoy_battery_state | Not Charging | mobile_app | 45851fa08a686298bbdd690959ea8a22 |  |  |  |
| sensor.gt_iphone16_tonmoy_bssid | unavailable | mobile_app | 45851fa08a686298bbdd690959ea8a22 |  |  |  |
| sensor.gt_iphone16_tonmoy_connection_type | unavailable | mobile_app | 45851fa08a686298bbdd690959ea8a22 |  |  |  |
| sensor.gt_iphone16_tonmoy_geocoded_location | unavailable | mobile_app | 45851fa08a686298bbdd690959ea8a22 |  |  |  |
| sensor.gt_iphone16_tonmoy_last_update_trigger | unavailable | mobile_app | 45851fa08a686298bbdd690959ea8a22 |  |  |  |
| sensor.gt_iphone16_tonmoy_location_permission | Authorized Always | mobile_app | 45851fa08a686298bbdd690959ea8a22 |  |  |  |
| sensor.gt_iphone16_tonmoy_sim_1 | unavailable | mobile_app | 45851fa08a686298bbdd690959ea8a22 |  |  |  |
| sensor.gt_iphone16_tonmoy_sim_2 | unavailable | mobile_app | 45851fa08a686298bbdd690959ea8a22 |  |  |  |
| sensor.gt_iphone16_tonmoy_ssid | unavailable | mobile_app | 45851fa08a686298bbdd690959ea8a22 |  |  |  |
| sensor.gt_iphone16_tonmoy_storage | unavailable | mobile_app | 45851fa08a686298bbdd690959ea8a22 |  |  |  |
| sensor.gt_iphone16_tonmoy_watch_battery_level | 60 | mobile_app | 45851fa08a686298bbdd690959ea8a22 |  |  |  |
| sensor.gt_iphone16_tonmoy_watch_battery_state | Not Charging | mobile_app | 45851fa08a686298bbdd690959ea8a22 |  |  |  |
| sensor.guest_apartment_today | Guests Staying | template | None |  |  |  |
| sensor.guest_room_effective_temp | unavailable | template | None |  |  |  |
| sensor.guest_sensor_battery | 100.0 | tuya | ef735cbfada97bad3bb720ff0583f902 |  |  |  |
| sensor.guest_sensor_humidity | 54.0 | tuya | ef735cbfada97bad3bb720ff0583f902 |  |  |  |
| sensor.guest_sensor_temperature | 18.0 | tuya | ef735cbfada97bad3bb720ff0583f902 |  |  |  |
| sensor.home_assistant_core_cpu_percent | unavailable_in_state_api | hassio | 38e891cbe0bbfc14782f7fc8b1970c88 |  | integration |  |
| sensor.home_assistant_core_memory_percent | unavailable_in_state_api | hassio | 38e891cbe0bbfc14782f7fc8b1970c88 |  | integration |  |
| sensor.home_assistant_host_apparmor_version | unavailable_in_state_api | hassio | 650599f0d7ecb9ce74b348add2a4be06 |  | integration |  |
| sensor.home_assistant_host_disk_free | unavailable_in_state_api | hassio | 650599f0d7ecb9ce74b348add2a4be06 |  | integration |  |
| sensor.home_assistant_host_disk_total | unavailable_in_state_api | hassio | 650599f0d7ecb9ce74b348add2a4be06 |  | integration |  |
| sensor.home_assistant_host_disk_used | unavailable_in_state_api | hassio | 650599f0d7ecb9ce74b348add2a4be06 |  | integration |  |
| sensor.home_assistant_host_os_agent_version | unavailable_in_state_api | hassio | 650599f0d7ecb9ce74b348add2a4be06 |  | integration |  |
| sensor.home_assistant_operating_system_newest_version | unavailable_in_state_api | hassio | e01721b13c409a5e69839135694e8dde |  | integration |  |
| sensor.home_assistant_operating_system_version | unavailable_in_state_api | hassio | e01721b13c409a5e69839135694e8dde |  | integration |  |
| sensor.home_assistant_supervisor_cpu_percent | unavailable_in_state_api | hassio | 011e3de6bc457a9cce31c216d0f0d1eb |  | integration |  |
| sensor.home_assistant_supervisor_memory_percent | unavailable_in_state_api | hassio | 011e3de6bc457a9cce31c216d0f0d1eb |  | integration |  |
| sensor.hp_laserjet_m109_m112 | idle | ipp | f2f3929cdf2d00acf9370b9fec00a39b |  |  |  |
| sensor.hp_laserjet_m109_m112_black_cartridge_hp_w1410a | 41 | ipp | f2f3929cdf2d00acf9370b9fec00a39b |  |  |  |
| sensor.hp_laserjet_m109_m112_uptime | unavailable_in_state_api | ipp | f2f3929cdf2d00acf9370b9fec00a39b |  | integration |  |
| sensor.internet_status | online | template | None |  |  |  |
| sensor.ipad_activity | Stationary | mobile_app | 4cbbd019c1c324f2830af3835a14573c |  |  |  |
| sensor.ipad_battery_level | 79 | mobile_app | 4cbbd019c1c324f2830af3835a14573c |  |  |  |
| sensor.ipad_battery_state | Not Charging | mobile_app | 4cbbd019c1c324f2830af3835a14573c |  |  |  |
| sensor.ipad_bssid | f0:2f:74:93:9f:6c | mobile_app | 4cbbd019c1c324f2830af3835a14573c |  |  |  |
| sensor.ipad_connection_type | Wi-Fi | mobile_app | 4cbbd019c1c324f2830af3835a14573c |  |  |  |
| sensor.ipad_geocoded_location | 38 Ken Douglas Dr Wellington Porirua 5024 New Zealand | mobile_app | 4cbbd019c1c324f2830af3835a14573c |  |  |  |
| sensor.ipad_last_update_trigger | Background Fetch | mobile_app | 4cbbd019c1c324f2830af3835a14573c |  |  |  |
| sensor.ipad_ssid | Tonmoy&Esha | mobile_app | 4cbbd019c1c324f2830af3835a14573c |  |  |  |
| sensor.ipad_storage | 17.39 | mobile_app | 4cbbd019c1c324f2830af3835a14573c |  |  |  |
| sensor.kira_cpu_usage | unavailable | template | None |  |  |  |
| sensor.kira_disk_usage | unavailable | template | None |  |  |  |
| sensor.kira_last_heartbeat | unavailable | template | None |  |  |  |
| sensor.kira_memory_usage | unavailable | template | None |  |  |  |
| sensor.kira_openclaw_memory_mb | unavailable | template | None |  |  |  |
| sensor.kira_openclaw_pid | unavailable | template | None |  |  |  |
| sensor.living_room_sensor_battery | 100.0 | tuya | 8c80629af94d96e413ca7b5e82273d4e |  |  |  |
| sensor.living_room_sensor_humidity | 41.0 | tuya | 8c80629af94d96e413ca7b5e82273d4e |  |  |  |
| sensor.living_room_sensor_temperature | 21.5 | tuya | 8c80629af94d96e413ca7b5e82273d4e |  |  |  |
| sensor.livingroom_echo_next_alarm | unavailable | alexa_media | a11ae81cda4fcd36480cbbea9a7f110d |  |  |  |
| sensor.livingroom_echo_next_reminder | unavailable | alexa_media | a11ae81cda4fcd36480cbbea9a7f110d |  |  |  |
| sensor.livingroom_echo_next_timer | unavailable | alexa_media | a11ae81cda4fcd36480cbbea9a7f110d |  |  |  |
| sensor.lounge_tv_next_alarm | unavailable | alexa_media | f2decf6933767a8ff8e35fc676be8cf3 |  |  |  |
| sensor.lounge_tv_next_reminder | unavailable | alexa_media | f2decf6933767a8ff8e35fc676be8cf3 |  |  |  |
| sensor.lounge_tv_next_timer | unavailable | alexa_media | f2decf6933767a8ff8e35fc676be8cf3 |  |  |  |
| sensor.macmini_active_audio_input | unavailable | mobile_app | 3d9f0e7360bc1439bb21d2abf7b38eab |  |  |  |
| sensor.macmini_active_audio_output | unavailable | mobile_app | 3d9f0e7360bc1439bb21d2abf7b38eab |  |  |  |
| sensor.macmini_active_camera | unavailable | mobile_app | 3d9f0e7360bc1439bb21d2abf7b38eab |  |  |  |
| sensor.macmini_app_version | 2026.4.1 | mobile_app | 3d9f0e7360bc1439bb21d2abf7b38eab |  |  |  |
| sensor.macmini_audio_output | unavailable | mobile_app | 3d9f0e7360bc1439bb21d2abf7b38eab |  |  |  |
| sensor.macmini_bssid | unavailable | mobile_app | 3d9f0e7360bc1439bb21d2abf7b38eab |  |  |  |
| sensor.macmini_connection_type | unavailable | mobile_app | 3d9f0e7360bc1439bb21d2abf7b38eab |  |  |  |
| sensor.macmini_cpu_usage | 28.3 | command_line | None |  |  |  |
| sensor.macmini_displays | unavailable | mobile_app | 3d9f0e7360bc1439bb21d2abf7b38eab |  |  |  |
| sensor.macmini_frontmost_app | unavailable | mobile_app | 3d9f0e7360bc1439bb21d2abf7b38eab |  |  |  |
| sensor.macmini_geocoded_location | unavailable | mobile_app | 3d9f0e7360bc1439bb21d2abf7b38eab |  |  |  |
| sensor.macmini_gpu_usage | 0 | command_line | None |  |  |  |
| sensor.macmini_last_update_trigger | unavailable | mobile_app | 3d9f0e7360bc1439bb21d2abf7b38eab |  |  |  |
| sensor.macmini_location_permission | Authorized Always | mobile_app | 3d9f0e7360bc1439bb21d2abf7b38eab |  |  |  |
| sensor.macmini_memory_usage | 45.5 | command_line | None |  |  |  |
| sensor.macmini_primary_display_id | unavailable | mobile_app | 3d9f0e7360bc1439bb21d2abf7b38eab |  |  |  |
| sensor.macmini_primary_display_name | unavailable | mobile_app | 3d9f0e7360bc1439bb21d2abf7b38eab |  |  |  |
| sensor.macmini_ssid | unavailable | mobile_app | 3d9f0e7360bc1439bb21d2abf7b38eab |  |  |  |
| sensor.macmini_storage | unavailable | mobile_app | 3d9f0e7360bc1439bb21d2abf7b38eab |  |  |  |
| sensor.macmini_storage_usage | 12 | command_line | None |  |  |  |
| sensor.master_bedroom_battery | 100.0 | tuya | 48f4a819cb987fee163b14ca194f808a |  |  |  |
| sensor.master_bedroom_echo_next_alarm | unavailable | alexa_media | b492ce0b5e267a94cf33335454ad23c9 |  |  |  |
| sensor.master_bedroom_echo_next_reminder | unavailable | alexa_media | b492ce0b5e267a94cf33335454ad23c9 |  |  |  |
| sensor.master_bedroom_echo_next_timer | unavailable | alexa_media | b492ce0b5e267a94cf33335454ad23c9 |  |  |  |
| sensor.master_bedroom_effective_temp | unavailable | template | None |  |  |  |
| sensor.master_bedroom_humidity | 51.0 | tuya | 48f4a819cb987fee163b14ca194f808a |  |  |  |
| sensor.master_bedroom_temperature | 20.4 | tuya | 48f4a819cb987fee163b14ca194f808a |  |  |  |
| sensor.matter_server_cpu_percent | unavailable_in_state_api | hassio | 4752365e039c0bd0a6e5295c3f68f2fb |  | integration |  |
| sensor.matter_server_memory_percent | unavailable_in_state_api | hassio | 4752365e039c0bd0a6e5295c3f68f2fb |  | integration |  |
| sensor.matter_server_newest_version | unavailable_in_state_api | hassio | 4752365e039c0bd0a6e5295c3f68f2fb |  | integration |  |
| sensor.matter_server_version | unavailable_in_state_api | hassio | 4752365e039c0bd0a6e5295c3f68f2fb |  | integration |  |
| sensor.mqtt_last_probe_age_seconds | 8046 | template | None |  |  |  |
| sensor.mqtt_service_status | offline | template | None |  |  |  |
| sensor.mqtt_telemetry_freshness | offline | template | None |  |  |  |
| sensor.nas_archive_usage_percent | 0.0 | command_line | None |  |  |  |
| sensor.nas_backups_usage_percent | 15.7 | command_line | None |  |  |  |
| sensor.nas_documents_usage_percent | 1.5 | command_line | None |  |  |  |
| sensor.nas_media_usage_percent | 82.2 | command_line | None |  |  |  |
| sensor.nas_total_usage | 3 | command_line | None |  |  |  |
| sensor.omarchy_cpu_usage | unavailable | template | None |  |  |  |
| sensor.omarchy_disk_usage | unavailable | template | None |  |  |  |
| sensor.omarchy_gpu_usage | unavailable | template | None |  |  |  |
| sensor.omarchy_last_seen | unavailable | template | None |  |  |  |
| sensor.omarchy_memory_usage | unavailable | template | None |  |  |  |
| sensor.openclaw_service_status | offline | template | None |  |  |  |
| sensor.outside_battery | unknown | ring | bb57207c1b9443ed2a2b6c0b6e288baf |  |  |  |
| sensor.outside_last_activity | 2026-05-15T23:07:38+00:00 | ring | bb57207c1b9443ed2a2b6c0b6e288baf |  |  |  |
| sensor.outside_signal_strength | unavailable_in_state_api | ring | bb57207c1b9443ed2a2b6c0b6e288baf |  | integration |  |
| sensor.outside_wi_fi_signal_category | unavailable_in_state_api | ring | bb57207c1b9443ed2a2b6c0b6e288baf |  | integration |  |
| sensor.plex_service_status | online | template | None |  |  |  |
| sensor.ps5_245_activity | unavailable | mqtt | 6becd5e1cd0fe305efadb99e47b51184 |  |  |  |
| sensor.refrigerator_fresh_air_filter | replace | lg_thinq | d0a70869a2eb8d5489a54fddde519f34 |  |  |  |
| sensor.refrigerator_water_filter | replace | lg_thinq | d0a70869a2eb8d5489a54fddde519f34 |  |  |  |
| sensor.refrigerator_water_filter_used | 6 | lg_thinq | d0a70869a2eb8d5489a54fddde519f34 |  |  |  |
| sensor.rt_ax86u_9f68_data_received | unavailable_in_state_api | upnp | 1d7f4de704ebd20b1627b8787d93a06d |  | integration |  |
| sensor.rt_ax86u_9f68_data_sent | unavailable_in_state_api | upnp | 1d7f4de704ebd20b1627b8787d93a06d |  | integration |  |
| sensor.rt_ax86u_9f68_download_speed | 31.8430383968422 | upnp | 1d7f4de704ebd20b1627b8787d93a06d |  |  |  |
| sensor.rt_ax86u_9f68_external_ip | 100.78.208.174 | upnp | 1d7f4de704ebd20b1627b8787d93a06d |  |  |  |
| sensor.rt_ax86u_9f68_number_of_port_mapping_entries_ipv4 | unavailable_in_state_api | upnp | 1d7f4de704ebd20b1627b8787d93a06d |  | integration |  |
| sensor.rt_ax86u_9f68_packet_download_speed | unavailable_in_state_api | upnp | 1d7f4de704ebd20b1627b8787d93a06d |  | integration |  |
| sensor.rt_ax86u_9f68_packet_upload_speed | unavailable_in_state_api | upnp | 1d7f4de704ebd20b1627b8787d93a06d |  | integration |  |
| sensor.rt_ax86u_9f68_packets_received | unavailable_in_state_api | upnp | 1d7f4de704ebd20b1627b8787d93a06d |  | integration |  |
| sensor.rt_ax86u_9f68_packets_sent | unavailable_in_state_api | upnp | 1d7f4de704ebd20b1627b8787d93a06d |  | integration |  |
| sensor.rt_ax86u_9f68_upload_speed | 55.8343874251973 | upnp | 1d7f4de704ebd20b1627b8787d93a06d |  |  |  |
| sensor.rt_ax86u_9f68_uptime | unavailable_in_state_api | upnp | 1d7f4de704ebd20b1627b8787d93a06d |  | integration |  |
| sensor.rt_ax86u_9f68_wan_status | unavailable_in_state_api | upnp | 1d7f4de704ebd20b1627b8787d93a06d |  | integration |  |
| sensor.study_echo_next_alarm | unavailable | alexa_media | fdad0809ca11ca6447f4f58bdf297e3d |  |  |  |
| sensor.study_echo_next_reminder | unavailable | alexa_media | fdad0809ca11ca6447f4f58bdf297e3d |  |  |  |
| sensor.study_echo_next_timer | unavailable | alexa_media | fdad0809ca11ca6447f4f58bdf297e3d |  |  |  |
| sensor.study_sensor_battery | unavailable | tuya | defedd9c7cc79a84a378eb002606088d |  |  |  |
| sensor.study_sensor_humidity | unavailable | tuya | defedd9c7cc79a84a378eb002606088d |  |  |  |
| sensor.study_sensor_temperature | unavailable | tuya | defedd9c7cc79a84a378eb002606088d |  |  |  |
| sensor.sun_next_dawn | 2026-05-16T18:52:58+00:00 | sun | 46c2ac25e3ed4d8b02630bd625ffe6bd |  |  |  |
| sensor.sun_next_dusk | 2026-05-16T05:41:26+00:00 | sun | 46c2ac25e3ed4d8b02630bd625ffe6bd |  |  |  |
| sensor.sun_next_midnight | 2026-05-16T12:17:00+00:00 | sun | 46c2ac25e3ed4d8b02630bd625ffe6bd |  |  |  |
| sensor.sun_next_noon | 2026-05-16T00:16:57+00:00 | sun | 46c2ac25e3ed4d8b02630bd625ffe6bd |  |  |  |
| sensor.sun_next_rising | 2026-05-16T19:23:19+00:00 | sun | 46c2ac25e3ed4d8b02630bd625ffe6bd |  |  |  |
| sensor.sun_next_setting | 2026-05-16T05:11:10+00:00 | sun | 46c2ac25e3ed4d8b02630bd625ffe6bd |  |  |  |
| sensor.sun_solar_azimuth | unavailable_in_state_api | sun | 46c2ac25e3ed4d8b02630bd625ffe6bd |  | integration |  |
| sensor.sun_solar_elevation | unavailable_in_state_api | sun | 46c2ac25e3ed4d8b02630bd625ffe6bd |  | integration |  |
| sensor.system_monitor_battery | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_battery_empty | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_cpu_pressure_some_10s_average | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_cpu_pressure_some_300s_average | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_cpu_pressure_some_60s_average | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_cpu_pressure_some_total | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_disk_free | 44.4 | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  |  |  |
| sensor.system_monitor_disk_free_config | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_disk_free_media | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_disk_free_run_audio | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_disk_free_share | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_disk_free_ssl | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_disk_usage | 20.2 | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  |  |  |
| sensor.system_monitor_disk_usage_config | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_disk_usage_media | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_disk_usage_run_audio | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_disk_usage_share | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_disk_usage_ssl | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_disk_use | 11.2 | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  |  |  |
| sensor.system_monitor_disk_use_config | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_disk_use_media | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_disk_use_run_audio | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_disk_use_share | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_disk_use_ssl | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_io_pressure_full_10s_average | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_io_pressure_full_300s_average | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_io_pressure_full_60s_average | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_io_pressure_full_total | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_io_pressure_some_10s_average | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_io_pressure_some_300s_average | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_io_pressure_some_60s_average | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_io_pressure_some_total | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_ipv4_address_docker0 | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_ipv4_address_enp1s0 | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_ipv4_address_enp2s0 | unavailable | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  |  |  |
| sensor.system_monitor_ipv4_address_hassio | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_ipv4_address_lo | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_ipv6_address_docker0 | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_ipv6_address_enp1s0 | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_ipv6_address_hassio | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_ipv6_address_lo | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_last_boot | 2026-05-15T20:55:12+00:00 | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  |  |  |
| sensor.system_monitor_load_15_min | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_load_1_min | 0.0 | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  |  |  |
| sensor.system_monitor_load_5_min | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_memory_free | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_memory_pressure_full_10s_average | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_memory_pressure_full_300s_average | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_memory_pressure_full_60s_average | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_memory_pressure_full_total | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_memory_pressure_some_10s_average | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_memory_pressure_some_300s_average | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_memory_pressure_some_60s_average | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_memory_pressure_some_total | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_memory_usage | 13.0 | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  |  |  |
| sensor.system_monitor_memory_use | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_network_in_docker0 | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_network_in_enp1s0 | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_network_in_hassio | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_network_in_lo | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_network_out_docker0 | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_network_out_enp1s0 | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_network_out_hassio | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_network_out_lo | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_network_throughput_in_docker0 | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_network_throughput_in_enp1s0 | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_network_throughput_in_enp2s0 | unavailable | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  |  |  |
| sensor.system_monitor_network_throughput_in_hassio | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_network_throughput_in_lo | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_network_throughput_out_docker0 | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_network_throughput_out_enp1s0 | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_network_throughput_out_enp2s0 | unavailable | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  |  |  |
| sensor.system_monitor_network_throughput_out_hassio | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_network_throughput_out_lo | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_packets_in_docker0 | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_packets_in_enp1s0 | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_packets_in_hassio | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_packets_in_lo | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_packets_out_docker0 | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_packets_out_enp1s0 | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_packets_out_hassio | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_packets_out_lo | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_processor_temperature | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_processor_use | 1 | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  |  |  |
| sensor.system_monitor_swap_free | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_swap_usage | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.system_monitor_swap_use | unavailable_in_state_api | systemmonitor | a2682f234290d78a1f6e912b9468ead5 |  | integration |  |
| sensor.tailscale_esha_iphone_last_seen | 2026-05-15T23:05:56+00:00 | template | None |  |  |  |
| sensor.tailscale_offline_device_names | none | template | None |  |  |  |
| sensor.tailscale_offline_devices | 0 | template | None |  |  |  |
| sensor.tailscale_online_device_names | Esha's iPhone, Tonmoy's iPhone, Tonmoy’s Mac mini, TonmoysLaptop | template | None |  |  |  |
| sensor.tailscale_online_devices | 4 | template | None |  |  |  |
| sensor.tailscale_service_status | offline | template | None |  |  |  |
| sensor.tailscale_tailnet_devices_raw | 4 | rest | None |  |  |  |
| sensor.tailscale_tonmoy_iphone_last_seen | 2026-05-15T23:05:56+00:00 | template | None |  |  |  |
| sensor.tailscale_total_devices | 4 | template | None |  |  |  |
| sensor.this_device_next_alarm_2 | unknown | alexa_media | 2707e067fe901832bf908d4deb1cb9ca |  |  |  |
| sensor.this_device_next_reminder_2 | unknown | alexa_media | 2707e067fe901832bf908d4deb1cb9ca |  |  |  |
| sensor.this_device_next_timer_2 | unknown | alexa_media | 2707e067fe901832bf908d4deb1cb9ca |  |  |  |
| sensor.today_s_meal | Leftovers | template | None |  |  |  |
| sensor.today_s_meal_cook_time | 10 minutes | template | None |  |  |  |
| sensor.today_s_meal_cuisine | Mixed | template | None |  |  |  |
| sensor.today_s_meal_ingredients | - Leftover cooked meals from earlier in the week - Optional quick sides: cucumber sticks, fruit, yogurt | template | None |  |  |  |
| sensor.today_s_meal_name | Leftovers | template | None |  |  |  |
| sensor.today_s_meal_recipe_file | /config/mealprep/Recipes/Leftovers.md | template | None |  |  |  |
| sensor.today_s_meal_servings | 3 | template | None |  |  |  |
| sensor.today_s_meal_status | ok | template | None |  |  |  |
| sensor.today_s_meal_steps | 1. Reheat leftovers to steaming hot. 2. Serve with a fresh side if needed. 3. Cool and refrigerate any remaining food promptly. | template | None |  |  |  |
| sensor.today_s_meal_summary | Today: Leftovers · 10 minutes · Serves 3 | template | None |  |  |  |
| sensor.todays_meal_data | Leftovers | command_line | None |  |  |  |
| sensor.tonmoy_s_ipad_activity | Stationary | mobile_app | 9418289693162d7abc44504ae08712e0 |  |  |  |
| sensor.tonmoy_s_ipad_battery_level | 100 | mobile_app | 9418289693162d7abc44504ae08712e0 |  |  |  |
| sensor.tonmoy_s_ipad_battery_state | Full | mobile_app | 9418289693162d7abc44504ae08712e0 |  |  |  |
| sensor.tonmoy_s_ipad_bssid | f0:2f:74:93:9f:6c | mobile_app | 9418289693162d7abc44504ae08712e0 |  |  |  |
| sensor.tonmoy_s_ipad_connection_type | Wi-Fi | mobile_app | 9418289693162d7abc44504ae08712e0 |  |  |  |
| sensor.tonmoy_s_ipad_geocoded_location | 40 Ken Douglas Dr Wellington Porirua 5024 New Zealand | mobile_app | 9418289693162d7abc44504ae08712e0 |  |  |  |
| sensor.tonmoy_s_ipad_last_update_trigger | Periodic | mobile_app | 9418289693162d7abc44504ae08712e0 |  |  |  |
| sensor.tonmoy_s_ipad_ssid | Tonmoy&Esha | mobile_app | 9418289693162d7abc44504ae08712e0 |  |  |  |
| sensor.tonmoy_s_ipad_storage | 32.55 | mobile_app | 9418289693162d7abc44504ae08712e0 |  |  |  |
| sensor.tonmoy_s_sony_wh_1000xm3_next_alarm | unavailable | alexa_media | 03904f513f0045a6baf94eb09be9c066 |  |  |  |
| sensor.tonmoy_s_sony_wh_1000xm3_next_timer | unavailable | alexa_media | 03904f513f0045a6baf94eb09be9c066 |  |  |  |
| sensor.tonmoynz_bronze_trophies | unavailable | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  |  |  |
| sensor.tonmoynz_gold_trophies | unavailable | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  |  |  |
| sensor.tonmoynz_last_online | unavailable | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  |  |  |
| sensor.tonmoynz_next_level | unavailable | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  |  |  |
| sensor.tonmoynz_now_playing | unavailable | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  |  |  |
| sensor.tonmoynz_online_id | unavailable | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  |  |  |
| sensor.tonmoynz_online_status | unavailable | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  |  |  |
| sensor.tonmoynz_platinum_trophies | unavailable | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  |  |  |
| sensor.tonmoynz_silver_trophies | unavailable | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  |  |  |
| sensor.tonmoynz_trophy_level | unavailable | playstation_network | d5d74eea9b41c73198534d7dd8c4ddc6 |  |  |  |
| sensor.tonmoysplexserver | 0 | plex | 134c03a7908c30788d042f4c6d9d18c9 |  |  |  |
| sensor.tonmoysplexserver_library_movies | 14 | plex | 134c03a7908c30788d042f4c6d9d18c9 |  |  |  |
| sensor.tonmoysplexserver_library_tv_shows | 0 | plex | 134c03a7908c30788d042f4c6d9d18c9 |  |  |  |
| sensor.washing_machine_current_status | power_off | lg_thinq | bb38c4bd14ab0724a436eaa871ba8ddb |  |  |  |
| sensor.washing_machine_cycles | 37 | lg_thinq | bb38c4bd14ab0724a436eaa871ba8ddb |  |  |  |
| sensor.washing_machine_delayed_end | unknown | lg_thinq | bb38c4bd14ab0724a436eaa871ba8ddb |  |  |  |
| sensor.washing_machine_remaining_time | unknown | lg_thinq | bb38c4bd14ab0724a436eaa871ba8ddb |  |  |  |
| sensor.washing_machine_total_time | unknown | lg_thinq | bb38c4bd14ab0724a436eaa871ba8ddb |  |  |  |
| sensor.zigbee_service_status | online | template | None |  |  |  |
| switch.advanced_ssh_web_terminal | unavailable_in_state_api | hassio | 64952aed9a0643b98c6cfaaa4a53d492 |  | integration |  |
| switch.alexa_media_player_pre_release | unavailable_in_state_api | hacs | 32936a89c07e401cea5646d18e933fe8 |  | integration |  |
| switch.apexcharts_card_pre_release | unavailable_in_state_api | hacs | d6440512f7f28cf2bc3760a1b2c1d5cc |  | integration |  |
| switch.auto_entities_pre_release | unavailable_in_state_api | hacs | 6567fd4c7c68fdd6056af0441be573fd |  | integration |  |
| switch.better_thermostat_ui_pre_release | unavailable_in_state_api | hacs | 18e7bffa27814f550e35fa25591cc7d6 |  | integration |  |
| switch.bubble_card_pre_release | unavailable_in_state_api | hacs | 499b1a0446b4e0126f607d0f14474ec7 |  | integration |  |
| switch.button_card_pre_release | unavailable_in_state_api | hacs | 6889e9f30bab3c7f0ac95d8236c4e214 |  | integration |  |
| switch.card_mod_pre_release | unavailable_in_state_api | hacs | 5cf8923f4cd057685c005c91f5bb2e2f |  | integration |  |
| switch.config_template_card_pre_release | unavailable_in_state_api | hacs | 17f1b27600565c80266fccf4f32c6d3f |  | integration |  |
| switch.dryer_power | off | lg_thinq | 090cf0d491e3bee0a7e74667a6f0faeb |  |  |  |
| switch.dyson_pre_release | unavailable_in_state_api | hacs | 9bba01d8123cc3818cf976fbb4a1bd06 |  | integration |  |
| switch.dyson_sz1_au_nja5315a_continuous_monitoring | on | hass_dyson | 1cb57f9d286501d415e6a9bca47f2450 |  |  |  |
| switch.dyson_sz1_au_nja5315a_firmware_auto_update | on | hass_dyson | 1cb57f9d286501d415e6a9bca47f2450 |  |  |  |
| switch.dyson_sz1_au_nja5315a_night_mode | off | hass_dyson | 1cb57f9d286501d415e6a9bca47f2450 |  |  |  |
| switch.everywhere_do_not_disturb | unavailable | alexa_media | c00a20fb321d83101668d15dea721951 |  |  |  |
| switch.everywhere_repeat | unavailable | alexa_media | c00a20fb321d83101668d15dea721951 |  |  |  |
| switch.everywhere_shuffle | unavailable | alexa_media | c00a20fb321d83101668d15dea721951 |  |  |  |
| switch.expander_card_pre_release | unavailable_in_state_api | hacs | d0cfef5a0879baee353afc244a34d1b5 |  | integration |  |
| switch.front_door_motion_detection | on | ring | 08d6efd50bb1b7bf4b601cfd1a941af1 |  |  |  |
| switch.gree_a_c_pre_release | unavailable_in_state_api | hacs | 644114405a5fda4206aac52952f0cd61 |  | integration |  |
| switch.ha_floorplan_your_imagination_almost_defines_the_limits_pre_release | unavailable_in_state_api | hacs | d0b2dd240afae10e7c54df7366c1bccf |  | integration |  |
| switch.hacs_pre_release | unavailable_in_state_api | hacs | d1ebeb2089e7a2bcd87a2c4e05a07c50 |  | integration |  |
| switch.kiosk_mode_pre_release | unavailable_in_state_api | hacs | 440f319327a4b0400a8a8a6fcd7dc42c |  | integration |  |
| switch.layout_card_pre_release | unavailable_in_state_api | hacs | d31cb9e882ea36545f8699e5dc9ed198 |  | integration |  |
| switch.livingroom_echo_do_not_disturb | unavailable | alexa_media | a11ae81cda4fcd36480cbbea9a7f110d |  |  |  |
| switch.livingroom_echo_repeat | unavailable | alexa_media | a11ae81cda4fcd36480cbbea9a7f110d |  |  |  |
| switch.livingroom_echo_shuffle | unavailable | alexa_media | a11ae81cda4fcd36480cbbea9a7f110d |  |  |  |
| switch.local_tuya_pre_release | unavailable_in_state_api | hacs | 8236fd986544a15f04dadf191ca530ec |  | integration |  |
| switch.lounge_tv_do_not_disturb | unavailable | alexa_media | f2decf6933767a8ff8e35fc676be8cf3 |  |  |  |
| switch.lounge_tv_repeat | unavailable | alexa_media | f2decf6933767a8ff8e35fc676be8cf3 |  |  |  |
| switch.lounge_tv_shuffle | unavailable | alexa_media | f2decf6933767a8ff8e35fc676be8cf3 |  |  |  |
| switch.lovelace_html_card_pre_release | unavailable_in_state_api | hacs | 4cc5492c7126d4386b6c683156e9d296 |  | integration |  |
| switch.master_bedroom_echo_do_not_disturb | unavailable | alexa_media | b492ce0b5e267a94cf33335454ad23c9 |  |  |  |
| switch.master_bedroom_echo_repeat | unavailable | alexa_media | b492ce0b5e267a94cf33335454ad23c9 |  |  |  |
| switch.master_bedroom_echo_shuffle | unavailable | alexa_media | b492ce0b5e267a94cf33335454ad23c9 |  |  |  |
| switch.matter_server | unavailable_in_state_api | hassio | 4752365e039c0bd0a6e5295c3f68f2fb |  | integration |  |
| switch.mini_graph_card_pre_release | unavailable_in_state_api | hacs | a98e7eab77d8f445afa3ae8253abd65e |  | integration |  |
| switch.minimalistic_area_card_pre_release | unavailable_in_state_api | hacs | 5895c6f67ef318873d5f7bc781c2129c |  | integration |  |
| switch.mushroom_pre_release | unavailable_in_state_api | hacs | 2f951ffd6b6cf48a3d2c6bba0b64cd20 |  | integration |  |
| switch.neo_smart_blinds_blue_pre_release | unavailable_in_state_api | hacs | 7685b7cdc7b061c49b0a348f850cb6c8 |  | integration |  |
| switch.outside_in_home_chime | on | ring | bb57207c1b9443ed2a2b6c0b6e288baf |  |  |  |
| switch.outside_motion_detection | on | ring | bb57207c1b9443ed2a2b6c0b6e288baf |  |  |  |
| switch.plex_meets_home_assistant_pre_release | unavailable_in_state_api | hacs | 80ab6d604b324983b542aacff1701113 |  | integration |  |
| switch.ps5 | unavailable | wake_on_lan | None |  |  |  |
| switch.ps5_245_power | unavailable | mqtt | 6becd5e1cd0fe305efadb99e47b51184 |  |  |  |
| switch.refrigerator_express_cool | off | lg_thinq | d0a70869a2eb8d5489a54fddde519f34 |  |  |  |
| switch.refrigerator_express_mode | off | lg_thinq | d0a70869a2eb8d5489a54fddde519f34 |  |  |  |
| switch.study_echo_do_not_disturb | unavailable | alexa_media | fdad0809ca11ca6447f4f58bdf297e3d |  |  |  |
| switch.study_echo_repeat | unavailable | alexa_media | fdad0809ca11ca6447f4f58bdf297e3d |  |  |  |
| switch.study_echo_shuffle | unavailable | alexa_media | fdad0809ca11ca6447f4f58bdf297e3d |  |  |  |
| switch.this_device_do_not_disturb_2 | off | alexa_media | 2707e067fe901832bf908d4deb1cb9ca |  |  |  |
| switch.tonmoy_s_sony_wh_1000xm3_do_not_disturb | unavailable | alexa_media | 03904f513f0045a6baf94eb09be9c066 |  |  |  |
| switch.tonmoy_s_sony_wh_1000xm3_repeat | unavailable | alexa_media | 03904f513f0045a6baf94eb09be9c066 |  |  |  |
| switch.tonmoy_s_sony_wh_1000xm3_shuffle | unavailable | alexa_media | 03904f513f0045a6baf94eb09be9c066 |  |  |  |
| switch.upcoming_media_card_pre_release | unavailable_in_state_api | hacs | 3d2cb4976086163eb018489745b7e31c |  | integration |  |
| switch.washing_machine_power | off | lg_thinq | bb38c4bd14ab0724a436eaa871ba8ddb |  |  |  |
| switch.wi_fi_power_strip_child_lock | unavailable | tuya | 6feb2d023c3351e2ce1001764cace3bb |  |  |  |
| switch.wi_fi_power_strip_socket_1 | unavailable | tuya | 6feb2d023c3351e2ce1001764cace3bb |  |  |  |
| switch.wi_fi_power_strip_socket_2 | unavailable | tuya | 6feb2d023c3351e2ce1001764cace3bb |  |  |  |
| switch.wi_fi_power_strip_socket_3 | unavailable | tuya | 6feb2d023c3351e2ce1001764cace3bb |  |  |  |
| switch.wi_fi_power_strip_socket_4 | unavailable | tuya | 6feb2d023c3351e2ce1001764cace3bb |  |  |  |
| switch.wi_fi_power_strip_socket_5 | unavailable | tuya | 6feb2d023c3351e2ce1001764cace3bb |  |  |  |
| todo.shopping_list | 0 | shopping_list | None |  |  |  |
| tts.google_translate_en_com | unknown | google_translate | 9d94c527af1d2b8c20319cd2887dde0f |  |  |  |
| update.advanced_ssh_web_terminal_update | off | hassio | 64952aed9a0643b98c6cfaaa4a53d492 |  |  |  |
| update.alexa_media_player_update | on | hacs | 32936a89c07e401cea5646d18e933fe8 |  |  |  |
| update.apexcharts_card_update | off | hacs | d6440512f7f28cf2bc3760a1b2c1d5cc |  |  |  |
| update.auto_entities_update | off | hacs | 6567fd4c7c68fdd6056af0441be573fd |  |  |  |
| update.better_thermostat_ui_update | off | hacs | 18e7bffa27814f550e35fa25591cc7d6 |  |  |  |
| update.bubble_card_update | off | hacs | 499b1a0446b4e0126f607d0f14474ec7 |  |  |  |
| update.button_card_update | off | hacs | 6889e9f30bab3c7f0ac95d8236c4e214 |  |  |  |
| update.card_mod_update | off | hacs | 5cf8923f4cd057685c005c91f5bb2e2f |  |  |  |
| update.config_template_card_update | off | hacs | 17f1b27600565c80266fccf4f32c6d3f |  |  |  |
| update.dyson_sz1_au_nja5315a_firmware_update | off | hass_dyson | 1cb57f9d286501d415e6a9bca47f2450 |  |  |  |
| update.dyson_update | on | hacs | 9bba01d8123cc3818cf976fbb4a1bd06 |  |  |  |
| update.expander_card_update | on | hacs | d0cfef5a0879baee353afc244a34d1b5 |  |  |  |
| update.gree_a_c_update | on | hacs | 644114405a5fda4206aac52952f0cd61 |  |  |  |
| update.ha_floorplan_your_imagination_almost_defines_the_limits_update | on | hacs | d0b2dd240afae10e7c54df7366c1bccf |  |  |  |
| update.hacs_update | off | hacs | d1ebeb2089e7a2bcd87a2c4e05a07c50 |  |  |  |
| update.home_assistant_core_update | on | hassio | 38e891cbe0bbfc14782f7fc8b1970c88 |  |  |  |
| update.home_assistant_operating_system_update | off | hassio | e01721b13c409a5e69839135694e8dde |  |  |  |
| update.home_assistant_supervisor_update | off | hassio | 011e3de6bc457a9cce31c216d0f0d1eb |  |  |  |
| update.kiosk_mode_update | on | hacs | 440f319327a4b0400a8a8a6fcd7dc42c |  |  |  |
| update.layout_card_update | off | hacs | d31cb9e882ea36545f8699e5dc9ed198 |  |  |  |
| update.local_tuya_update | off | hacs | 8236fd986544a15f04dadf191ca530ec |  |  |  |
| update.lovelace_html_card_update | off | hacs | 4cc5492c7126d4386b6c683156e9d296 |  |  |  |
| update.matter_server_update | off | hassio | 4752365e039c0bd0a6e5295c3f68f2fb |  |  |  |
| update.mini_graph_card_update | off | hacs | a98e7eab77d8f445afa3ae8253abd65e |  |  |  |
| update.minimalistic_area_card_update | off | hacs | 5895c6f67ef318873d5f7bc781c2129c |  |  |  |
| update.mushroom_update | off | hacs | 2f951ffd6b6cf48a3d2c6bba0b64cd20 |  |  |  |
| update.neo_smart_blinds_blue_update | off | hacs | 7685b7cdc7b061c49b0a348f850cb6c8 |  |  |  |
| update.plex_meets_home_assistant_update | off | hacs | 80ab6d604b324983b542aacff1701113 |  |  |  |
| update.tonmoysplexserver_update | on | plex | 134c03a7908c30788d042f4c6d9d18c9 |  |  |  |
| update.upcoming_media_card_update | off | hacs | 3d2cb4976086163eb018489745b7e31c |  |  |  |
| weather.forecast_home | cloudy | met | 27c809895e08af921e0ff095a1303034 |  |  |  |

## Integration List

| Entry ID | Domain | Title | State | Source | Disabled By |
| --- | --- | --- | --- | --- | --- |
| 01KHNS760VDKTTZXX106E7A7SW | alexa_media | tonmoy.rahman@gmail.com - amazon.com | loaded | user |  |
| 01KHNHNHZE2202WW30B51J6TGE | apple_tv | Living room | loaded | zeroconf |  |
| 01KHMEG52N5VJ6GFVVFJ9MS7E1 | backup | Backup | loaded | system |  |
| 01KHWCVDY7A03GV3N9SKQGX3WZ | dlna_dmr | Samsung The Frame 65 | loaded | ssdp |  |
| 01KJVXPB030KPYC57A1WMDK60T | dlna_dms | Plex Media Server: TonmoysPlexServer | loaded | ssdp |  |
| 01KHMGQAY5T1P6YYVXT880XDGE | google_translate | Google Translate text-to-speech | loaded | onboarding |  |
| 01KHMHZBSPRH5SHF1TMQXXVGKZ | hacs |  | loaded | user |  |
| 01KJTNT1P6Q5CCKDB48M3Z9AAC | hass_dyson | Dyson Account (tonmoy.rahman@gmail.com) | loaded | user |  |
| 01KJTTQ9QGTDBR6GQQQSQ29W4A | hass_dyson | Garage | loaded | device_auto_create |  |
| 01KJS5PVW7W0CR1RERMYBZDJN9 | hassio | Supervisor | loaded | system |  |
| 01KJW8Z0EVXF4G09M2F5ZJBNTW | homekit | Front Door Live view:21068 | loaded | accessory |  |
| 01KJW8Z0EWTXQ0BAQX6R698DQM | homekit | HASS Bridge 0H:21065 | loaded | user |  |
| 01KJS5PTFP46EQX18SWXJNN750 | homekit | HASS Bridge:21064 | loaded | user |  |
| 01KJW8Z0EVF5DTN5VVX5187MMR | homekit | Outside Live view:21067 | loaded | accessory |  |
| 01KJW8Z0EP5YWE17VCGC3ZVBQ1 | homekit | PlayStation 5:21066 | loaded | accessory |  |
| 01KK8JRH65JK2XNS1HNHBXFNFH | ios | Home Assistant iOS | loaded | user |  |
| 01KJSF4D4W88C4XB66X07K9MD3 | ipp | HP LaserJet M110w (A88C55) | loaded | zeroconf |  |
| 01KJSF035EZYMMG7QEY0NXTYMJ | lg_thinq | LG ThinQ | loaded | user |  |
| 01KK5TC1R7ZAK4PPESS5BE7K14 | localtuya | tonmoy.rahman@gmail.com | loaded | user |  |
| 01KJSF7M61NDENKAF1J4MJH4PB | matter | Matter | loaded | zeroconf |  |
| 01KHMGQAYFGE4395ZJW78PR5GJ | met | Home | loaded | onboarding |  |
| 01KHNHZAG9S9FXWHAC4MW968F8 | mobile_app | Esha’s iPhone | loaded | registration |  |
| 01KJS8FXNW4K7P0DR9B213T0WB | mobile_app | GT-iPhone16-Tonmoy | loaded | registration |  |
| 01KK0CK5KE2CS4XNC7T761FJGH | mobile_app | MacMini | loaded | registration |  |
| 01KJV9E7HWJZX53PY29TCMJWAE | mobile_app | Tonmoy's iPad | loaded | registration |  |
| 01KKDTBEP5RHVZ1M2ZY0T2QQ4Z | mobile_app | iPad | loaded | registration |  |
| 01KJVNZBXA704AJXQS3XJ0Y1GZ | mqtt | Mosquitto Mqtt Broker | loaded | user |  |
| 01KKMS08ZYXKQBC7PQJYJN1AV4 | ping | 1.1.1.1 | loaded | user |  |
| 01KKNM3693K1QXWTGY2ESW0X4Y | ping | 192.168.50.100 | loaded | user |  |
| 01KKNJVYQJGE6B9T9RVBG3VS4C | ping | 8.8.8.8 | loaded | user |  |
| 01KJVGYW53XF1Z99NQKSJ2EA3E | playstation_network | tonmoyNZ | setup_error | user |  |
| 01KHYJGZ8ZVCPF9RV5BA2KEHYF | plex | https://192-168-50-208.14f210ee7d154a76be1cc99f224d6d84.plex.direct:32400 | loaded | zeroconf |  |
| 01KHMGQAW02JEZHC6D3EMY61J6 | radio_browser | Radio Browser | loaded | onboarding |  |
| 01KJW4YC9YF60W546X3FBT991V | remote_calendar | Airbnb | loaded | user |  |
| 01KJW4X8RJHNW9ZGAXSDVVXXB3 | remote_calendar | BookingDotCom | loaded | user |  |
| 01KJW0XHZ5G430AZJ5KXX20HZM | ring | tonmoy.rahman@gmail.com | loaded | user |  |
| 01KHMGQARFBN4RF8Y0VKKAG33Q | shopping_list | Shopping list | loaded | onboarding |  |
| 01KHMEG49ATMWG6P48E5SGCE9Q | sun | Sun | loaded | import |  |
| 01KKMRZBGWREKMBJ9898KBJY9W | systemmonitor | System Monitor | loaded | user |  |
| 01KHNNJXYDNB3085P9GW8DR01G | thread | Thread | loaded | zeroconf |  |
| 01KRNK4YHXHXGN9A8S1BC5BM52 | tuya | tonmoy.rahman@gmail.com | loaded | user |  |
| 01KJSF4XFM48B2AM8GCNYPRKHX | upnp | RT-AX86U-9F68 | loaded | ssdp |  |

## Add-on Inventory

| Name | Slug | Version | State | Update Available | Repository |
| --- | --- | --- | --- | --- | --- |
| Advanced SSH & Web Terminal | a0d7b954_ssh | 23.0.9 | started | False | a0d7b954 |
| Matter Server | core_matter_server | 8.4.0 | started | False | core |

## Automation Inventory

| Entity ID | State | Alias | Automation ID | Last Triggered | Mode |
| --- | --- | --- | --- | --- | --- |
| automation.alexa_sync_dining_blind_1 | off | Alexa: Sync Dining Blind 1 | 2a97cc4db5c542ed8293399bd518dde0 |  | single |
| automation.alexa_sync_dining_blind_2 | off | Alexa: Sync Dining Blind 2 | 929c95d1eec0431e8c09c95a6d8f58fe |  | single |
| automation.alexa_sync_living_room_blind | off | Alexa: Sync Living Room Blind | 422b23b589fb4787bd2452f38bcc4d2d |  | single |
| automation.alexa_sync_master_bedroom_blind | off | Alexa: Sync Master Bedroom Blind | 8ce876dad1774dc2b10018aa78d57392 |  | single |
| automation.alexa_sync_sophie_s_blind | off | Alexa: Sync Sophie's Blind | 604ea00bf0054432ae72ac242ef66cf5 |  | single |
| automation.alexa_sync_study_blind | off | Alexa: Sync Study Blind | cca6e676d3324368b4cf794108a9e839 |  | single |
| automation.auto_start_heater | on | Auto start heater | 1772541597347 | 2026-05-10T18:11:42.505936+00:00 | single |
| automation.mealprep_refresh_today_s_meal_every_15_min | unavailable | MealPrep - Refresh Today's Meal every 15 min | mealprep_refresh_every_15min |  |  |
| automation.mealprep_refresh_today_s_meal_on_ha_start | unavailable | MealPrep - Refresh Today's Meal on HA start | mealprep_refresh_on_start |  |  |
| automation.new_automation | on | Auto heater off | 1772542171241 | 2026-05-10T23:46:50.712422+00:00 | single |
| automation.openclaw_self_recovery | on | OpenClaw Self Recovery | openclaw_self_recovery_20260314 | 2026-05-08T22:59:52.687982+00:00 | single |
| automation.set_ac_fan_speed_from_slider | on | Set AC Fan Speed From Slider | 65a17456a2764a9f943a1cc5070751cf | 2026-03-14T02:47:13.660062+00:00 | single |

## NAS Storage Architecture

- NAS host: **Mac Mini** (`192.168.50.208`)
- SMB share: **`Plex_HD`**
- Local path on this host: `/Volumes/Plex_HD`

### Linux automount configuration

`/etc/systemd/system/home-tonmoy-nas.mount`
```ini

```

`/etc/systemd/system/home-tonmoy-nas.automount`
```ini

```

### `/etc/fstab` NAS-related entries
```fstab
```

### Folder structure under `Plex_HD` (depth <= 3)
```text
/Volumes/Plex_HD/.Trash-1000
/Volumes/Plex_HD/.Trash-1000/files
/Volumes/Plex_HD/.Trash-1000/files/.obsidian
/Volumes/Plex_HD/.Trash-1000/files/Archive
/Volumes/Plex_HD/.Trash-1000/files/HomeAssistant
/Volumes/Plex_HD/.Trash-1000/files/ROMs
/Volumes/Plex_HD/.Trash-1000/info
/Volumes/Plex_HD/.fseventsd
/Volumes/Plex_HD/Archive
/Volumes/Plex_HD/Backups
/Volumes/Plex_HD/Backups/Games
/Volumes/Plex_HD/Backups/Games/ROMs
/Volumes/Plex_HD/Backups/HomeAssistant
/Volumes/Plex_HD/Backups/MacMini
/Volumes/Plex_HD/Documents
/Volumes/Plex_HD/Documents/Kira
/Volumes/Plex_HD/Documents/MealPrep
/Volumes/Plex_HD/Documents/MealPrep/.backups
/Volumes/Plex_HD/Documents/MealPrep/.status
/Volumes/Plex_HD/Documents/MealPrep/Recipes
/Volumes/Plex_HD/Documents/MealPrep/config
/Volumes/Plex_HD/Documents/MealPrep/inventory
/Volumes/Plex_HD/Documents/Projects
/Volumes/Plex_HD/Documents/Sketchup
/Volumes/Plex_HD/Documents/Work
/Volumes/Plex_HD/Documents/Work/CV
/Volumes/Plex_HD/Documents/Work/Job Application
/Volumes/Plex_HD/Documents/Work/LinkedIn
/Volumes/Plex_HD/Documents/Work/Offers
/Volumes/Plex_HD/Media
/Volumes/Plex_HD/Media/Movies
/Volumes/Plex_HD/Media/Movies/Barbarian.2022.1080p.WEB.H264-NAISU
/Volumes/Plex_HD/Media/Movies/La Haine (1995) [1080p] [BluRay] [5.1] [YTS.MX]
/Volumes/Plex_HD/Media/Movies/Longlegs.2024.1080p.AMZN.WEB-DL.DDP5.1.H.264-BYNDR[TGx]
/Volumes/Plex_HD/Media/Movies/Materialists (2025) [1080p] [BluRay] [5.1] [YTS.MX]
/Volumes/Plex_HD/Media/Movies/Shall We Dance (1996) [1080p] [BluRay] [5.1] [YTS.MX]
/Volumes/Plex_HD/Media/Movies/Sling.Blade.Directors.Cut.1996.1080p.BluRay.x264.AAC-ETRG
/Volumes/Plex_HD/Media/Movies/The Thin Red Line (1998) [1080p]
/Volumes/Plex_HD/Media/Movies/The.Menu.2022.1080p.WEBRip.1400MB.DD5.1.x264-GalaxyRG[TGx]
/Volumes/Plex_HD/Media/Movies/The.Whale.2022.1080p.10bit.BluRay.6CH.x265.HEVC-PSA
/Volumes/Plex_HD/Media/Movies/www.UIndex.org    -    It Was Just An Accident (2025) 1080p WEBRip x265 10bit 5.1-WORLD
/Volumes/Plex_HD/Media/Music
/Volumes/Plex_HD/Media/TV Shows
```

## Backup Locations

- Home Assistant local backup store (`.local`)
- NAS backup folders observed:
  - `/Volumes/Plex_HD/Backups/HomeAssistant`
  - `/Volumes/Plex_HD/Backups/Home_assistant`
  - `/Volumes/Plex_HD/Backups/MacMini`

| Date | Slug | Name | Type | Size(MB) | Locations | Protected |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-05-15T17:11:21.016698+00:00 | ceb42f30 | Automatic backup 2026.4.1 | partial | 113.65 | None | False |
| 2026-05-11T17:25:09.143323+00:00 | a9a49f80 | Automatic backup 2026.4.1 | partial | 112.36 | None | True |

## Tailscale Remote Access Architecture

_Tailscale status was unavailable during generation._

## Failure Scenarios

1. **HA Core unavailable** — automation/control outage on the dedicated Wyse 5070 appliance.
2. **Mac Mini NAS unavailable** — media + backup share access interrupted, but HA should remain online.
3. **Tailscale subnet router (HAOS thin client) offline** — remote access to LAN/HA interrupted. The Mac Mini no longer acts as a subnet router.
4. **Neo blinds hub or local LAN issue** — cover state/control degradation.
5. **Supervisor add-on failure** (MQTT/Matter/etc.) — integration-specific impact.

## Recovery Procedures

### A) Home Assistant outage
1. Confirm HA host reachability on `192.168.50.166:8123`.
2. If host is offline, troubleshoot the Wyse 5070 appliance directly (power, network link, local SSD/boot state).
3. If host alive but HA down: restart HA Core from supervisor/UI.
4. If corruption suspected: restore latest healthy backup from HA backup store (no VM snapshot path assumed).
5. Validate critical integrations: covers, climate, MQTT, mobile app.

### B) NAS mount failure (`/Volumes/Plex_HD`)
1. Check Mac Mini reachability: `ping 192.168.50.208`.
2. On macOS, confirm `/Volumes/Plex_HD` is mounted; on Omarchy, restart automount units:
   - `sudo systemctl restart home-tonmoy-nas.automount home-tonmoy-nas.mount`
3. Verify mount: `ls /Volumes/Plex_HD`.
4. If auth fails on Omarchy, verify credentials file `/home/tonmoy/.smb/macmini`.

### C) Tailscale remote path failure
1. On this node: `tailscale status` and check health warnings.
2. Verify HAOS thin client (`homeassistant` tailnet node) is online and advertising route `192.168.50.0/24`.
3. Restart Tailscale add-on in HA (Settings → Apps → Tailscale → Restart) if needed.
4. Fall back to local LAN access for emergency operations.

### D) Blinds state desync
1. Use dashboard **Refresh Blind Status** action (calls `homeassistant.update_entity`).
2. Prefer Alexa control via HA-exposed entities to preserve state integrity.
3. Verify cover entities update in Developer Tools → States.

