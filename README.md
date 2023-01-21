create env
```bash
conda create -n wineq python=3.9 -y
```

activate env
```bash
conda activate wineq
```

created a req file

install the req
```
pip install - requirements.txt
```

downlaod the data from

https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing
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
git add . && git commit -m "update Readme.md"
```
```bash
git remote add origin https://github.com/praj2408/simple-dvc-demo.git
```
```bash
git branch -M main
```
```bash
git push origin main
```