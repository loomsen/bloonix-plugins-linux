CONFIG=Makefile.config

include $(CONFIG)

default: build

build:

install:
	if test ! -e "$(PREFIX)/lib/bloonix/plugins" ; then \
		mkdir -p $(PREFIX)/lib/bloonix/plugins; \
		chmod 755 $(PREFIX)/lib/bloonix/plugins; \
	fi;

	cd plugins; for file in check-* ; do \
		cp $$file $(PREFIX)/lib/bloonix/plugins/; \
		chmod 755 $(PREFIX)/lib/bloonix/plugins/$$file; \
	done;

	if test ! -e "$(PREFIX)/lib/bloonix/etc/plugins/linux" ; then \
		mkdir -p $(PREFIX)/lib/bloonix/etc/plugins/; \
		chmod 755 $(PREFIX)/lib/bloonix/etc/plugins/; \
	fi;

	cd plugins; for file in plugin-* ; do \
		cp $$file $(PREFIX)/lib/bloonix/etc/plugins/; \
		chmod 644 $(PREFIX)/lib/bloonix/etc/plugins/$$file; \
	done;

	mkdir -p /etc/bloonix/agent/sudoers.d;
	cp -a sudoers/* /etc/bloonix/agent/sudoers.d/;

clean:
