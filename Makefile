VENV = venv
PYTHON = $(VENV)\Scripts\python
PIP = $(VENV)\Scripts\pip
DIR = assignment


hello: 
	@echo "The program is starting!"


define create-venv
python -m venv $(VENV)
endef

run: $(VENV)\Scripts\activate
	$(PYTHON) $(DIR)\app.py

read_sql: run
	$(PYTHON) $(DIR)\sql_read.py

run_test: $(VENV)\Scripts\activate
	$(PYTHON) $(DIR)\get_holidays_test.py
	@echo "test completed"

$(VENV)\Scripts\activate: requirements.txt
	@$(create-venv)
	@$(VENV)\Scripts\activate
	@$(PIP) install -r requirements.txt


clean:
	@find . -name db.sqlite3 -delete
