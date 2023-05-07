run-linter:
	flake8 hw/code/*/*.py

run-tests:
	pytest --alluredir=allure-results hw/code/test*.py
	