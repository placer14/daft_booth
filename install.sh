#!/bin/sh

mv "./daft_booth_service.sh" "/etc/init.d/daft_booth_service.sh"
touch "/var/log/daft_booth.log" && chown "mg" "/var/log/daft_booth.log"
update-rc.d "daftbooth" defaults
service "daftbooth" start
