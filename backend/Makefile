PYTHONPATH ?= $$(pwd)/src
PYTHONPATH_DJANGO ?= ${PYTHONPATH}:$$(pwd)/src/apps
PYTHON ?= python
PYTHON_W_PATH ?= PYTHONPATH=${PYTHONPATH_DJANGO} python
DJANGO_SETTINGS ?= project.settings.development
MAKE_NO_PRINT = ${MAKE} --no-print-directory

.PHONY: install
install: .venv .django.env tls-init
	@echo "**************\nInstall Python dependencies via Poetry...\n"
	@${MAKE_NO_PRINT} python-install
	@echo "\n\n**************\nCreating our app migrations files...\n"
	@${MAKE_NO_PRINT} django-manage CMD='makemigrations'
	@echo "\n\n**************\nApplying all migrations to the database...\n"
	@${MAKE_NO_PRINT} django-manage CMD='migrate'
	@echo "\n\n**************\nCreating fixtures...\n"


.PHONY: django-runserver
django-runserver:
	@${MAKE_NO_PRINT} django-manage CMD="runserver 127.0.0.1:9000"


.PHONY: django-shell
django-shell: CMD_ARGS ?=
django-shell:
	@${MAKE_NO_PRINT} django-manage CMD="shell ${CMD_ARGS}"

.PHONY: django-manage
django-manage:
	@[ "${VIRTUAL_ENV}" ] || ( echo "! Virtualenv not detected - type 'source .venv/bin/activate' to activate it."; exit 1 )
	@[ "${CMD}" ] || ( echo "! Make variable CMD is not set"; exit 1 )
	@DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS} ${PYTHON_W_PATH} src/manage.py ${CMD}


.PHONY: makemigrations
makemigrations:
	@${MAKE_NO_PRINT} django-manage CMD='makemigrations ${ARGS}'


.PHONY: migrate
migrate:
	@${MAKE_NO_PRINT} django-manage CMD='migrate'

.PHONY: run-tests
run-tests: ARGS ?= --cov=src --cov-config=.coveragerc --cov-report html
run-tests:
	@[ "${VIRTUAL_ENV}" ] || ( echo "! Virtualenv not detected - type 'source .venv/bin/activate' to activate it."; exit 1 )
	@${PYTHON_W_PATH} -m pytest ${ARGS}

.PHONY: python-code-quality
python-code-quality:
# Bash-Fu is my greatest passion. (NO)
	@exit_codes=0 ; \
		${MAKE_NO_PRINT} python-black ; exit_codes=$$(( $$exit_codes + $$? )) ; \
		${MAKE_NO_PRINT} python-pylint ; exit_codes=$$(( $$exit_codes + $$? )) ; \
		${MAKE_NO_PRINT} python-mypy ; exit_codes=$$(( $$exit_codes + $$? )) ; \
		exit $$exit_codes


.PHONY: python-black
python-black: OPTS ?=
python-black:
	@[ "${VIRTUAL_ENV}" ] || ( echo "! Virtualenv not detected - type 'source .venv/bin/activate' to activate it."; exit 1 )
	@${PYTHON_W_PATH} -m black ${OPTS} src/

.PHONY: python-pylint
python-pylint:
	@[ "${VIRTUAL_ENV}" ] || ( echo "! Virtualenv not detected - type 'source .venv/bin/activate' to activate it."; exit 1 )
	@${PYTHON_W_PATH} -m pylint \
		project \
		authentication \
		core \
		dashboard \
		data_streaming \
		analytics \
		journal


.PHONY: python-mypy
python-mypy:
	@[ "${VIRTUAL_ENV}" ] || ( echo "! Virtualenv not detected - type 'source .venv/bin/activate' to activate it."; exit 1 )
	@MYPYPATH=${PYTHONPATH_DJANGO} ${PYTHON_W_PATH} -m mypy src/
