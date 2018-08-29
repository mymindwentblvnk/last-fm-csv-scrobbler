venv:
	virtualenv -p python3 venv && . venv/bin/activate && pip install -r requirements.txt && deactivate

process:
	. venv/bin/activate && python main.py && deactivate
