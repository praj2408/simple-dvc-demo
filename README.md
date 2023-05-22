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
