# ETL Pipelines & Star Schema for Data Warehousing
## Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides locally in CSV and JSON files as well as in S3 cloud storage as JSON files, all containing user activity logs on their app.

The goal is to build an ETL pipeline that extracts their data from multiple sources separetly, transforms it to facts and dimentions for a Star Schema model and store them in different database solutions (PostgreSQL, Cassandra, AWS Redshift).
