from pyspark.sql import SparkSession
from src.pipeline import run_pipeline

# Prompt user for parameters
while True:
    try:
        TOP_N = int(input("Enter how many top movies to display (e.g., 10): "))
        MIN_RATINGS = int(input("Enter minimum number of ratings to include a movie (e.g., 100): "))
        break
    except ValueError:
        print("Invalid input. Please enter integers.")

# Initialize Spark
spark = SparkSession.builder.appName("MovieLens100K SQL Project").getOrCreate()

# Load data
ratings = spark.read.csv("data/u.data", sep="\t", inferSchema=True) \
    .toDF("user_id", "item_id", "rating", "timestamp")

movies = spark.read.csv("data/u.item", sep="|", inferSchema=True, encoding="ISO-8859-1") \
    .toDF("item_id", "title", "release_date", "video_release_date", "IMDb_URL",
          "unknown", "Action", "Adventure", "Animation", "Children's", "Comedy", "Crime",
          "Documentary", "Drama", "Fantasy", "Film-Noir", "Horror", "Musical", "Mystery",
          "Romance", "Sci-Fi", "Thriller", "War", "Western")

# Run the pipeline with parameters
run_pipeline(spark, ratings, movies, TOP_N, MIN_RATINGS)

spark.stop()
