#!/bin/sh
/usr/sbin/peervpn /mod/etc/peervpn.conf &
sleep 20
PEERVPN_PID=$(pidof peervpn)
kill -20 $PEERVPN_PID
kill -18 $PEERVPN_PID
exit 0

