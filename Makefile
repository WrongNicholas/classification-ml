VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
MAIN = main.py
REQ = requirements.txt

all: run

$(VENV):
	python3 -m venv $(VENV)

install: $(VENV)
	$(PIP) install --upgrade pip
	@if [ -f $(REQ) ]; then $(PIP) install -r $(REQ); fi

run: install
	$(PYTHON) $(MAIN)

clean:
	rm -rf $(VENV)
