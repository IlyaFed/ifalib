#Makefile

test:
	python setup.py pytest

pip: git clean
	python setup.py sdist bdist_wheel --universal # Universal mean python2/3
	twine upload dist/ifalib-*.tar.gz

clean:
	rm -f ifalib/*.so
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist

git: clean
	git add *
	git commit -m "New commit"
	git push
