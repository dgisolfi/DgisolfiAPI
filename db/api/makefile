repo=`grep __title__ ./CouchClient/__version__.py | grep -o '"[^"]\+"' | cut -d '"' -f2`
version=`grep __version__ ./CouchClient/__version__.py | grep -o '"[^"]\+"' | cut -d '"' -f2`

intro:
	@echo "$(repo) v$(version)"

init:
	@python3 -m pip install pipenv 
	@python3 -m pipenv install --dev
	@echo "Now run: pipenv shell"

clean:
	-rm -rf ./build ./dist ./__pycache__/
	-rm -rf ./$(repo)/$(repo).egg-info ./.eggs ./$(repo).egg-info
	-rm -f *.pyc *.pyo *.pyd *\$$py.class

build: init doc
	-pipenv run pipenv-setup sync
	@python3 setup.py sdist bdist_wheel

install: init
	@python3 -m pipenv run pipenv-setup sync
	@python3 -m pip install .

uninstall:
	echo "python3 -m pip uninstall $(repo)==$(version) -y"
	@python3 -m pip uninstall $(repo)==$(version) -y

sort_imports:
	isort -rc --atomic .
	# if this fails run pipenv shell and install dev
MAKE:
	intro
	install

.PHONY: intro init clean build install uninstall sort_imports
