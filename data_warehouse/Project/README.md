#Data warehouse project

This project using data from [Million Song Dataset](https://labrosa.ee.columbia.edu/millionsong/).
The purpose of this project is build ETL data pipe line with a database can hosted in AWS Redshift and it can be use to analyze and query data and answer question (example like what most common song users are listening to) .

## About data
There are 2 dataset:
*1. Song Dataset
File in Json format to store meta data about song and artist

*2. Log Dataset
File in Json format too, it recorded logs from a music streaming app.
In this project, we will load only the row if "page" column equal to "NextSong"


## Create Table
We will create following table with column:
*1. Dimention table
    users: userId, firstName, lastName, gender, level
    songs: song_id, title, artist_id, year, duration
    artists: artist_id, artist_name, artist_location, artist_latitude, artist_longitude
    time: start_time, hour, day, week, month, year, weekday
*2. Fact table
    songplay:  start_time, user_id, level, song_id, artist_id, session_id,  location, user_agent

## ETL Pipeline
These are step to create and load data stored in S3 to Redshift
1. Drop the table if it exist
2. Create table: staging, dimension and fact table
3. Copy data from S3 to staging table
4. Insert data from staging table to fact and dimension table

## To run programe
Open Jupyter notebook terminal.
Key in commanand bellow to execute data:

python create_tables.py
python etl.py
