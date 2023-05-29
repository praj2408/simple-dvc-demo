create env
```bash
conda create -p wineq python==3.8 -y
```

activate env
```bash
activate wineq/
```

created a req file
install the requirements
```bash
pip install -r requirements.txt
```
download the data from the above link
```bash
git init
```
```bash
dvc init
```
```bash
dvc add data_given/winequality.csv
```
```bash
git add .
```
```bash
git commit -m "first commit"
```
```bash
dvc repro
```

tox command - 
```bash
tox
```
for rebuilding - 
```bash
tox -r
```

pytest command -
```bash
pytest -v
```

setup commands -
```bash
pip install -e .
```

build your own package command - 
```bash
python setup.py sdist bdist_wheel
```

changing branch -
```bash
git checkout -b main-mlflow
```

mlflow server command -

mlflow server
--backend-store-uri sqlite:///mlflow.db
--default-artifact-root ./artifacts
--host 0.0.0.0 -p 1234