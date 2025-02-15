# Projeto Ações Backend

This is a Django-based backend API for retrieving stock market data using **Yahoo Finance (`yfinance`)**.  
It supports **custom time ranges**, caching with **Redis**, and is deployed on **Render**.  

---

### 1. Clone the Repository
```sh
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### 2. Make sure you have Python 3.10+ and pipenv installed.

```sh
pip install pipenv  
pipenv install
```

### 3. Apply Migrations & Run the Server

```sh
pipenv run python manage.py migrate
pipenv run python manage.py runserver
```
Now, the API should be running at:
http://localhost:8000
