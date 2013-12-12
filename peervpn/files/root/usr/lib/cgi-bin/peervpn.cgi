#!/bin/sh

. /usr/lib/libmodcgi.sh


#

sec_begin '$(lang de:"Starttyp" en:"Start type")'

cgi_print_radiogroup_service_starttype "enabled" "$TINC_ENABLED" "" "" 0

sec_end

#

sec_begin '$(lang de:"Konfiguration" en:"Configuration")'

cgi_print_textline_p "networkname" "$PEERVPN_NETWORKNAME" 25/255 "$(lang de:"networkname" en:"networkname"): "
cgi_print_password_p "psk" "$PEERVPN_PSK" 25/255 "$(lang de:"psk" en:"psk"): "
cgi_print_textline_p "initpeers" "$PEERVPN_INITPEERS" 25/255 "$(lang de:"initpeers" en:"initpeers"): "
cgi_print_textline_p "enabletunneling" "$PEERVPN_ENABLETUNNELING" 25/255 "$(lang de:"enabletunneling" en:"enabletunneling"): "
cgi_print_textline_p "interface" "$PEERVPN_INTERFACE" 25/255 "$(lang de:"interface" en:"interface"): "
cgi_print_textline_p "ifconfig4" "$PEERVPN_IFCONFIG4" 25/255 "$(lang de:"ifconfig4" en:"ifconfig4"): "
cgi_print_textline_p "ifconfig6" "$PEERVPN_IFCONFIG6" 25/255 "$(lang de:"ifconfig6" en:"ifconfig6"): "
cgi_print_textline_p "upcmd" "$PEERVPN_UPCMD" 25/255 "$(lang de:"upcmd" en:"upcmd"): "
cgi_print_textline_p "local" "$PEERVPN_LOCAL" 25/255 "$(lang de:"local" en:"local"): "
cgi_print_textline_p "port" "$PEERVPN_PORT" 25/255 "$(lang de:"port" en:"port"): "
cgi_print_textline_p "sockmark" "$PEERVPN_SOCKMARK" 25/255 "$(lang de:"sockmark" en:"sockmark"): "
cgi_print_textline_p "enableipv4" "$PEERVPN_ENABLEIPV4" 25/255 "$(lang de:"enableipv4" en:"enableipv4"): "
cgi_print_textline_p "enableipv6" "$PEERVPN_ENABLEIPV6" 25/255 "$(lang de:"enableipv6" en:"enableipv6"): "
cgi_print_textline_p "enablendpcache" "$PEERVPN_ENABLENDPCACHE" 25/255 "$(lang de:"enablendpcache" en:"enablendpcache"): "
cgi_print_textline_p "enablerelay" "$PEERVPN_ENABLERELAY" 25/255 "$(lang de:"enablerelay" en:"enablerelay"): "
cgi_print_textline_p "engine" "$PEERVPN_ENGINE" 25/255 "$(lang de:"engine" en:"engine"): "
cgi_print_textline_p "enableprivdrop" "$PEERVPN_ENABLEPRIVDROP" 25/255 "$(lang de:"enableprivdrop" en:"enableprivdrop"): "
cgi_print_textline_p "user" "$PEERVPN_USER" 25/255 "$(lang de:"user" en:"user"): "
cgi_print_textline_p "group" "$PEERVPN_GROUP" 25/255 "$(lang de:"group" en:"group"): "
cgi_print_textline_p "chroot" "$PEERVPN_CHROOT" 25/255 "$(lang de:"chroot" en:"chroot"): "

sec_end
