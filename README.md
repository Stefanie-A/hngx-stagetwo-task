# HNGX stagetwo task

![uml.png](./uml.png)

This repository contains the code and documentation for a simple REST api built with flask

## Prerequisites

- [Python](https://python.org) 3.9 or higher
- [Git](https://git-scm.com) 

## How to run

Clone the github repository
```bash
git clone https://github.com/Stefanie-A/hngx-stagetwo-task
```

Create a file called `.env` and add the following environment variables
- DATABASE_HOST: This refers to the url of your postgres server

- DATABASE_PORT: This refers to the port of your postgres server

- DATABASE_USER: This is the user to be used when logging into the database

- DATABASE_PASSWORD: This is the postgres password

Next, install required dependencies with `pip install -r requirements.txt`

Next, run database migrations with `flask db migrate` and `flask db upgrade`

Then, run the api with `python app.py` or `flask run`

## Usage

Documentation on how to use the API can be found [here](./DOCUMENTATION.md)