# Data Modeling with PostgreSQL

<a href="https://www.repostatus.org/#active"><img src="https://www.repostatus.org/badges/latest/active.svg" alt="Project Status: Active – The project has reached a stable, usable state and is being actively developed." /></a>

## Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like to create a Postgres database with tables designed to optimize queries on song play analysis. The project goal is to create a database schema and ETL pipeline for this analysis. We will be able to test the database and ETL pipeline by running queries given by the analytics team from Sparkify and compare our results with their expected results.

## Project Description
The main tasks are to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

## Setup
### Environment Variables :
The project uses a ```.env``` file containing the following enviroment variables which you can setup for yourself:
```
DB_HOST=172.0.0.1
DB_NAME=sparkifydb
DB_USERNAME=pg_username
DB_PASSWORD=pg_password
```
