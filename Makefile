# Use bash as the shell
SHELL := /bin/bash

# Makefile for a Flask project with Authlib and Jinja2

# Configuration
VENV_PATH=/mnt/o/venv/flask-jinja2-authlib
PYTHON=${VENV_PATH}/Scripts/python.exe

# Default target executed when no arguments are given to make.
default: setup

# Setup the virtual environment and install dependencies
setup: 
	@echo "Activating virtual environment..."
	source ${VENV_PATH}/Scripts/activate && ${PYTHON} -m pip install -r requirements.txt

# Run the Flask application
run:
	@echo "Activating virtual environment..."
	source ${VENV_PATH}/Scripts/activate && ${PYTHON} app.py

# Run tests (assuming you have a test suite setup)
test:
	@echo "Activating virtual environment..."
	source ${VENV_PATH}/Scripts/activate && ${PYTHON} -m unittest discover -s tests

# Clean up the project (remove pyc files, etc.)
clean:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete

# Activate the virtual environment
activate:
	@echo "To activate the virtual environment, run 'source ${VENV_PATH}/Scripts/activate'"

