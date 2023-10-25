REPOS_PATH = ~/Repos/Perso/aliases

all: test

test:
	pytest
	@if [ $$? -eq 0 ]; then \
		$(MAKE) -s build; \
	fi

.SILENT:
build:
	cp app.py $(REPOS_PATH)
	chmod 770 $(REPOS_PATH)
