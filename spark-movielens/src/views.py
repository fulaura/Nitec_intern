from pyspark.sql.functions import from_unixtime, year, month

def create_temp_views(spark, ratings_df, movies_df):
    # Enrich ratings with year/month
    ratings_df = ratings_df.withColumn("year", year(from_unixtime("timestamp"))) \
                           .withColumn("month", month(from_unixtime("timestamp")))

    # Register base views
    ratings_df.createOrReplaceTempView("ratings")
    movies_df.createOrReplaceTempView("movies_raw")

    # Join and create main working view
    spark.sql("""
        CREATE OR REPLACE TEMP VIEW ratings_with_titles AS
        SELECT r.*, 
               m.title, m.release_date, m.video_release_date, m.IMDb_URL,
               m.`unknown`, m.`Action`, m.`Adventure`, m.`Animation`, m.`Children's`,
               m.`Comedy`, m.`Crime`, m.`Documentary`, m.`Drama`, m.`Fantasy`,
               m.`Film-Noir`, m.`Horror`, m.`Musical`, m.`Mystery`, m.`Romance`,
               m.`Sci-Fi`, m.`Thriller`, m.`War`, m.`Western`
        FROM ratings r
        JOIN movies_raw m ON r.item_id = m.item_id
    """)
