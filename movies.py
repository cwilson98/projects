# import library
from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder.master("local").appName('movies').getOrCreate()
#
# Read in the csv files
idol_df = spark.read.option('header',True) \
               .option('delimiter',",") \
               .option("inferschema",True) \
               .csv(r"C:/Users/Chris/PycharmProjects/Projects/DA_Projects/movies/credits.csv")

titles_df = spark.read.option('header',True) \
                      .option('delimiter',',') \
                      .option("inferschema",True) \
                      .csv(r"C:/Users/Chris/PycharmProjects/Projects/DA_Projects/movies/titles.csv")

# Clean the data - Before I explore the data, I need to clean up any bad data



# print(idol_df.columns)
idol_df = idol_df.withColumnRenamed('id','film_id') \
                 .drop('person_id')
# print(idol_df.columns)

# titles_df.show(5,truncate=False)

# print(titles_df.columns)
titles_df = titles_df.withColumnRenamed('id','film_id') \
                     .withColumnRenamed('age_certification', 'rating') \
                     .na.fill("Other",['rating']) \
                     .drop("description")
# print(titles_df.columns)

# titles_df.show(5,truncate=False)
television_df = titles_df.filter(titles_df['type'] == "SHOW") \
                         .withColumnRenamed('title','show')
television_df = television_df.na.fill("Other",['production_countries']) \
                             .na.fill(0,['seasons'])
television_df = television_df.filter(television_df['release_year'] >= 1945)
# television_df.show(30,truncate=False)

movies_df = titles_df.filter(titles_df['type'] == "MOVIE") \
                         .withColumnRenamed('title','movie')
movies_df = movies_df.na.fill("Other",['production_countries']) \
                     .drop('seasons')
movies_df = movies_df.filter(movies_df['release_year'] >= 1945)

imdb_df = titles_df.select("film_id","imdb_id","imdb_score","imdb_votes")
# imdb_df.show(5,truncate=False)

tmdb_df = titles_df.select("film_id","tmdb_popularity","tmdb_score")
# tmdb_df.show(5,truncate=False)

# print(movies_df.columns)
movies_df = movies_df.drop("tmdb_popularity","tmdb_score","imdb_id","imdb_score","imdb_votes")
# movies_df.show(truncate=False)

# print(television_df.columns)
television_df = television_df.drop("tmdb_popularity","tmdb_score","imdb_id","imdb_score","imdb_votes")
# print(television_df.columns)

# Explore the data - I want to create any views that might be worth looking at in the future

television_temp_table = television_df.createOrReplaceTempView("television")
movies_temp_table = movies_df.createOrReplaceTempView("movies")
idol_temp_table = idol_df.createOrReplaceTempView("idol")
imdb_temp_table = imdb_df.createOrReplaceTempView("imdb")
tmdb_temp_table = tmdb_df.createOrReplaceTempView("tmdb")

# basic_query = """ SELECT *
#                   FROM television
#                   ORDER BY release_year DESC """
# spark.sql(basic_query).show(truncate=False)

# Which year had the most shows
# year_with_most_shows = """ SELECT release_year, COUNT(title) as num_of_shows
#                            FROM television
#                            WHERE release_year >= 1945
#                            GROUP BY release_year
#                            ORDER BY 2 DESC """
# spark.sql(year_with_most_shows).show(n=50,truncate=False)

# Which television show had the highest imdb score
# show_with_highest_scores = """ SELECT show, imdb_score
#                                FROM television
#                                 INNER JOIN imdb ON television.film_id = imdb.film_id
#                                ORDER BY imdb_score DESC """
# spark.sql(show_with_highest_scores).show(10,truncate=False)

# Which television rating had the highest tmdb score
# top_scores_per_rating = """ SELECT show, tmdb_score
#                             FROM television
#                                 INNER JOIN tmdb ON television.film_id = tmdb.film_id
#                             ORDER BY tmdb_score DESC """
# spark.sql(top_scores_per_rating).show(10,truncate=False)

# Which year had the highest number of votes
# show_with_most_votes = """ SELECT show, imdb_votes
#                            FROM television
#                             INNER JOIN imdb ON television.film_id = imdb.film_id
#                            ORDER BY 2 DESC"""
# spark.sql(film_with_most_votes).show(n=5,truncate=False)

# Which year had the most movies
# year_with_most_movies = """ SELECT release_year, COUNT(title) as num_of_movies
#                            FROM television
#                            WHERE release_year >= 1945
#                            GROUP BY release_year
#                            ORDER BY 2 DESC """
# spark.sql(year_with_most_shows).show(n=50,truncate=False)

# Which movie had the highest imdb score
# movie_with_highest_scores = """ SELECT movie, imdb_score
#                                FROM television
#                                 INNER JOIN imdb ON television.film_id = imdb.film_id
#                                ORDER BY imdb_score DESC """
# spark.sql(show_with_highest_scores).show(10,truncate=False)

# Which movie rating had the highest tmdb score
# top_scores_per_rating = """ SELECT movie, tmdb_score
#                             FROM television
#                                 INNER JOIN tmdb ON television.film_id = tmdb.film_id
#                             ORDER BY tmdb_score DESC """
# spark.sql(top_scores_per_rating).show(10,truncate=False)

# Which movie had the highest number of votes
# movie_with_most_votes = """ SELECT movie, imdb_votes
#                            FROM television
#                             INNER JOIN imdb ON television.film_id = imdb.film_id
#                            ORDER BY 2 DESC"""
# spark.sql(show_with_most_votes).show(n=5,truncate=False)




# End spark session
spark.stop()