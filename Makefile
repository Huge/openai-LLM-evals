.PHONY: mypy
mypy:
	mypy --config-file=mypy.ini --no-site-packages .

install:
	if [ ! -d ".venv" ]; then  virtualenv .venv; fi
	. .venv/bin/activate && pip3 install . && pip install jsonlines python-box

install-via-poetry:
	poetry add jsonlines
	poetry add python-box
	poetry install
