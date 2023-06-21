# install all the python package from requirements.txt in editable mode
deps:
	pip install --upgrade pip
	pip install -r requirements.txt
	pip install --editable .
	( \
       . .env/bin/activate; \
    )

# create python3 virtual environment .env
dev-env:
	python3 -m venv .env

# run all the test cases.
test:
	python -m unittest discover tests "*_test.py"
	pytest