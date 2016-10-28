INSTALL = install

install:
	[ -d $(HOME)/bin ] || mkdir $(HOME)/bin
	$(INSTALL) -m 755 ./tmcs $(HOME)/bin/tmcs
	[ -e $(HOME)/.tmcs.yml ] || $(INSTALL) -m 644 ./contrib/tmcs.yml $(HOME)/.tmcs.yml
