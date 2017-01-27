MANAGE=django-admin.py
SETTINGS=fortytwo_test_task.settings

test: check_noqa
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) test
	flake8 --exclude '*migrations*,fortytwo_test_task/settings/__init__.py' \
		--max-complexity=6 apps fortytwo_test_task

check_noqa:
	bash check_noqa.sh

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) syncdb --noinput

migrate:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) migrate

collectstatic:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(SETTINGS) $(MANAGE) collectstatic --noinput

custom:
    bash ls

all:
    cd some_dir; echo "I'm in some_dir"; \
          gcc -Wall -o myTest myTest.c

.PHONY: test syncdb migrate
