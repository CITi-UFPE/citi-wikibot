clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -delete
	rm -fr citi_wikibot.egg-info .egg htmlcov

dependencies:
	pip install coverage codecov pylint twine sphinx requests misaka -e .

readme:
	# install m2r: pip install m2r
	rm README.rst
	m2r README.md

publish:
	make readme clean
	python setup.py sdist
	twine upload dist/*
	rm -fr build dist .egg citi_wikibot.egg-info

test:
	coverage run -m unittest discover
	coverage xml
