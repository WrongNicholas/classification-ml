VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
PART1 = part1.py
PART2 = part2.py
REQ = requirements.txt

all: run

$(VENV):
	python3 -m venv $(VENV)

install: $(VENV)
	$(PIP) install --upgrade pip
	@if [ -f $(REQ) ]; then $(PIP) install -r $(REQ); fi

run1: install
	$(PYTHON) $(PART1)

run2: install
	$(PYTHON) $(PART2)

clean:
	rm -rf $(VENV)
