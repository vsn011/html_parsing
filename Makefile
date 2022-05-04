VENV = venv
DIR = assignment
IMAGE = py_app
CONTAINER = py_run


ifeq ($(shell echo "check_quotes"),"check_quotes")
   WINDOWS := yes
   PYTHON = $(VENV)/Scripts/python
   PIP = $(VENV)/Scripts/pip
else
   WINDOWS := no
   PYTHON = $(VENV)/bin/python3
   PIP = $(VENV)/bin/pip
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
	@$(VENV)/Scripts/activate
	@$(PIP) install -r requirements.txt


clean:
	del db/*.db

docker:
	docker build . -t $(IMAGE)
	docker run --name $(CONTAINER) $(IMAGE) python assignment/app.py