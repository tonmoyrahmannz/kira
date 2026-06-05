# Kira Morning Briefing Source Pull

Collected: 2026-05-17T03:13:02+12:00

## Home Assistant
- airbnb: off
- booking_com: on
- garage_temperature: 17.2 °C
- guest_apartment_today: No Guests Today
- guest_bedroom_humidity: 60.0 %
- guest_bedroom_temperature: 18.1 °C
- living_room_humidity: 51.0 %
- living_room_temperature: 19.4 °C
- master_bedroom_humidity: 56.0 %
- master_bedroom_temperature: 18.6 °C
- study_humidity: unavailable %
- study_temperature: unavailable °C
- weather_home: partlycloudy

## Calendar Next 24 Hours
- Calendar read failed: Command '['/usr/bin/osascript', '-e', '\nset nowDate to current date\nset endDate to nowDate + (24 * hours)\nset outputText to ""\ntell application "Calendar"\n    launch\n    repeat with c in calendars\n        try\n            set matchingEvents to every event of c whose start date is greater than or equal to nowDate and start date is less than or equal to endDate\n            repeat with e in matchingEvents\n                set eventLine to (summary of e) & " | " & ((start date of e) as string) & " | " & ((end date of e) as string) & " | " & (name of c)\n                set outputText to outputText & eventLine & linefeed\n            end repeat\n        end try\n    end repeat\nend tell\nreturn outputText\n']' timed out after 8 seconds

## Reminders
- no incomplete reminders returned

## Shortcut Runtime
- shortcuts CLI available: True
- matching shortcuts: Update Family Shopping List, MealPrep-Old_sync
