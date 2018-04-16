graph_mining
==============================

Project for the course "Graph Mining" during winter term 2017/18 at HPI

Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── report             <- Generated analysis as LaTeX
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    └── src                <- Source code for use in this project.
--------

## Data Preparation

- Put `hackernews.zip` in `data/raw/`  
- Uncompress the ZIP file: `unzip data/raw/hackernews.zip -d data/raw`  
- Uncompress the bzip2 files: `bzip2 -d data/raw/*.bz2`
- Make sure that the CSV files are in `data/raw/hackernews/`

## Setup

- Install the required Python libraries  
`pip install -r requirements.txt`  
- For topic modeling using MALLET, you have to install [MALLET](http://mallet.cs.umass.edu/) e.g. by  
`wget http://mallet.cs.umass.edu/dist/mallet-2.0.7.tar.gz && tar zxf mallet-2.0.7.tar.gz`

## Report
[Source](https://github.com/WGierke/graph_mining/blob/master/report/Finding_Hidden_Communities_in_HackerNews.pdf)
![finding_hidden_communities_in_hackernews-1](https://user-images.githubusercontent.com/6676439/38811847-f83141e8-418a-11e8-8cac-7a635b041bba.jpg)
![finding_hidden_communities_in_hackernews-2](https://user-images.githubusercontent.com/6676439/38811848-f8537f38-418a-11e8-8c9b-49e34c335ee6.jpg)
![finding_hidden_communities_in_hackernews-3](https://user-images.githubusercontent.com/6676439/38811849-f8776e20-418a-11e8-8512-8b580f47a449.jpg)
![finding_hidden_communities_in_hackernews-4](https://user-images.githubusercontent.com/6676439/38811850-f89b1622-418a-11e8-8489-e7a5eabd6db3.jpg)
