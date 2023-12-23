# Laporan Tugas UAS TESTING QA - Mohamad Ilman Huda

## Biodata
Nama : Mohamad Ilman huda \
Kelas : 07TPLE007 \
Mata Kuliah : Testing QA

# Tugas UAS
## Melengkapi fungsi test_post_cart

![run fungsi test_post_card](https://github.com/hudilman/simplecart-pytest-cicd/blob/main/img/Screen%20Shot%202023-12-22%20at%2019.54.56.png?raw=true)

Hasil pytest nya
![run fungsi test_post_card](https://github.com/hudilman/simplecart-pytest-cicd/blob/main/img/Screen%20Shot%202023-12-22%20at%2019.57.05.png?raw=true)

## Membuat Ci / Github Actions yang dapat menjalankan pytest dan pytest coverage, hasil dari gagal dan success nya

![github actions](https://github.com/hudilman/simplecart-pytest-cicd/blob/main/img/cicd.png?raw=true)

## Install Requirement

## Feature
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)&nbsp;&nbsp;
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/2.2.x/)

## Install requirements

    pip install -r requirements.txt
## create database
create new database, in this case we're using postgresql

## set env variable

create file .env in the root of the folder, and fill with you credential of your database

      
    DB_USER = ""
    DB_PASSWORD = ""
    DB_HOST = ""
    DB_PORT = ""
    DB_NAME = ""
    FLASK_DEBUG = true

## Create table

run `flask create`to create tables from models.

## Insert data product

run this query from your db client
```
INSERT INTO public.product (sku,brand,"name",description,price,non_discountable) VALUES
	 ('ABCKM5','ABC','kecap manis ABC 500ml','kecap manis abc 500ml',25000.0,false),
	 ('INDOSKM25','Indofood','Susu kental manis 250ml','Susu kental manis 250ml',15000.0,false),
	 ('LIOML1','Lion','Mamalemon 1000ml ','Mamalemon 1000ml ',21000.0,false),
	 ('INDOBR','Indofood','Bumbu racik','Bumbu racik',2500.0,false),
	 ('ABCS25','ABC','Sambal 250ml','Sambal 250ml',15000.0,false),
	 ('INDOIGS','Indofood','Indomie goreng special','Indomie goreng special',3000.0,false),
	 ('MYRLM1','mayora','le minerale 1000ml','le minerale 1000ml',8000.0,true);
```

## Run the app
to run the web app simply  use

    flask run

to access swagger use url `localhost:5000/apidocs`


## Run test
run test

    pytest

check test coverage

    pytest --cov=myproj tests/

## Debt

 - Cart Update
 - Same product validation on cart
 - Unit test
 - Unit test coverage
 - CI setup 


