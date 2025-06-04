# Build project
.PHONY = build
build:
	pip3 install -r requirements.txt

# Install dependencies
.PHONY = deps
deps:
	pip3 install -r requirements.txt

# Run tests
.PHONY = test
test:
	python3 -m unittest discover -s ./tests -p '*_test.py'

# Run full app
.PHONY = run
run:
	python3 main.py
