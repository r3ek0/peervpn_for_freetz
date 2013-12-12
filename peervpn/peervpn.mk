$(call PKG_INIT_BIN,0-036)
$(PKG)_SOURCE:=$(pkg)-$($(PKG)_VERSION).tar.gz
$(PKG)_SOURCE_MD5:=38fe86fed7ec341887220626cd102ec1
$(PKG)_SITE:=http://www.peervpn.net/files/
$(PKG)_BINARY:=$($(PKG)_DIR)/peervpn
$(PKG)_TARGET_BINARY:=$($(PKG)_DEST_DIR)/usr/sbin/peervpn

$(PKG_SOURCE_DOWNLOAD)
$(PKG_UNPACKED)
$(PKG_CONFIGURED_NOP)

$($(PKG)_BINARY): $($(PKG)_DIR)/.configured
	$(SUBMAKE) -C $(PEERVPN_DIR) \
		CC="$(TARGET_CC)" \
		CFLAGS="$(TARGET_CFLAGS)"

$($(PKG)_TARGET_BINARY): $($(PKG)_BINARY)
	$(INSTALL_BINARY_STRIP)

$(pkg):

$(pkg)-precompiled: $($(PKG)_TARGET_BINARY)

$(pkg)-clean:
	-$(SUBMAKE) -C $(PEERVPN_DIR) clean

$(pkg)-uninstall:
	$(RM) $(PEERVPN_TARGET_BINARY)

$(PKG_FINISH)
