VENV = venv
PYTHON = $(VENV)/Scripts/python3
PIP = $(VENV)/Scripts/pip


# run:
# 	python app.py
	
	
# hello:
# 	echo "this is my first make file"

venv/bin/activate: requirements.txt
	python -m venv $(VENV)
	$(VENV)\Scripts\activate
	$(PIP) install -r requirements.txt