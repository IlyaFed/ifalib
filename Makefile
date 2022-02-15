#Makefile

test:
	python setup.py pytest

test_gcc:
	${MAKE} -C tests test

pip: git clean test
	python setup.py sdist bdist_wheel --universal # Universal mean python2/3
	twine upload dist/ifalib-*.tar.gz

clean:
	rm -f ifalib/*.so
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist

git: clean doxy
	git add *
	git commit -m "Create step_to_compare in neighbour"
	git push

activate:
	source ifa/bin/activate

doxy:
	doxygen Doxyfile