all: test wheel

test: install
	python setup.py pytest

install:
	python setup.py install

wheel: install
	python setup.py bdist_wheel

