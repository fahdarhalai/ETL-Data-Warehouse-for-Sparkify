# Data Warehousing with AWS Redshift

## Introduction
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

The goal is to build an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to. We will be able to test the database and ETL pipeline by running queries given by the analytics team from Sparkify and compare our results with their expected results.

## Project Description
In this project, we will build an ETL pipeline for a database hosted on Redshift. Data is going to be loaded from S3 to staging tables on Redshift and execute SQL statements that create the analytics tables from these staging tables.

## Setup
To run the project, it is required to configure a Redshift database and an IAM role. Then create a file ```dwh.cfg``` in the root folder.
