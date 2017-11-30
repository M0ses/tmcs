PREFIX ?= /usr/local

INSTALL = install

install:
	[ -d $(DESTDIR)$(PREFIX)/bin ] || mkdir -p $(DESTDIR)$(PREFIX)/bin
	$(INSTALL) -m 755 ./tmcs $(DESTDIR)$(PREFIX)/bin/tmcs
