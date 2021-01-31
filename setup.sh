#!/bin/bash

sudo dnf check-update

sudo dnf install sugar-toolkit-gtk3 dbus-x11 *telemetry* telepathy* python2-devel \
python3-devel 
