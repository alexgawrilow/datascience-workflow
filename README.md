# Data Science Workflow
This repository serves as a reference for myself for a typical data science workflow that includes a tabular data set and a prediction task. Of course there does not exists a template that serves for every data science use case, but I tried to make the reference general.
As an use case the data science workflow is applied for the allknown titanic survival prediction problem from kaggle. The data set can be downloaded directly from kaggle.
The repository includes jupyter notebooks for the exploration part and the prediction part, each for the titanic use case and as a template for generic use. For reproducing the steps in the workflow the typical used data science packages have to be installed for python.

## Clone this repository
```
git clone
cd repository
``` 

## (Optional) Installation of dependencies
- Dependencies can be installed into a virtual environment using poetry.
```
poetry install
```

## (Optional) Install kernel for jupyter notebook
```
source .venv/bin/activate
ipython kernel install --user --name=titanic
```
Kernel can be used after opening a jupyter notebook and selecting Kernel --> Change kernel --> titanic
