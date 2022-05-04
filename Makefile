VENV = venv
DIR = assignment
IMAGE = py_app
CONTAINER = py_run
CMD = python -m pytest assignment/get_holidays_test.py


ifeq ($(shell echo "check_quotes"),"check_quotes")
   WINDOWS := yes
   PYTHON = $(VENV)/Scripts/python
   PIP = $(VENV)/Scripts/pip
   VENV_ACTIVATE = . $(VENV)/Scripts/activate
else
   WINDOWS := no
   PYTHON = $(VENV)/bin/python
   PIP = $(VENV)/bin/pip
   VENV_ACTIVATE = . $(VENV)/bin/activate
endif


hello: 
	@echo "This is my first Makefile"


define create-venv
python -m venv $(VENV)
endef

run: venv
	$(PYTHON) $(DIR)/app.py

read_sql: run
	$(PYTHON) $(DIR)/sql_read.py

run_test: venv
	$(PYTHON) -m pytest $(DIR)/get_holidays_test.py
	@echo "test completed"

venv: requirements.txt
	@$(create-venv)
	@$(VENV_ACTIVATE)
	@$(PIP) install -r requirements.txt


docker:
	docker build . -t $(IMAGE)
	docker run --rm --name $(CONTAINER) $(IMAGE) $(CMD)