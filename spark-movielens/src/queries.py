def top_rated_movies(spark, top_n, min_ratings):
    return spark.sql(f"""
        SELECT title, COUNT(rating) AS num_ratings, ROUND(AVG(rating), 2) AS avg_rating
        FROM ratings_with_titles
        GROUP BY title
        HAVING num_ratings > {min_ratings}
        ORDER BY avg_rating DESC
        LIMIT {top_n}
    """)

def average_rating_by_genre(spark):
    return spark.sql("""
        SELECT genre, COUNT(rating) AS num_ratings, ROUND(AVG(rating), 2) AS avg_rating
        FROM (
            SELECT title, rating,
                stack(19,
                    "Action", `Action`,
                    "Adventure", `Adventure`,
                    "Animation", `Animation`,
                    "Children's", `Children's`,
                    "Comedy", `Comedy`,
                    "Crime", `Crime`,
                    "Documentary", `Documentary`,
                    "Drama", `Drama`,
                    "Fantasy", `Fantasy`,
                    "Film-Noir", `Film-Noir`,
                    "Horror", `Horror`,
                    "Musical", `Musical`,
                    "Mystery", `Mystery`,
                    "Romance", `Romance`,
                    "Sci-Fi", `Sci-Fi`,
                    "Thriller", `Thriller`,
                    "War", `War`,
                    "Western", `Western`
                ) AS (genre, is_genre)
            FROM ratings_with_titles
        ) WHERE is_genre = 1
        GROUP BY genre
        ORDER BY avg_rating DESC
    """)

def ratings_by_year(spark):
    return spark.sql("""
        SELECT year, COUNT(rating) AS num_ratings, ROUND(AVG(rating), 2) AS avg_rating
        FROM ratings_with_titles
        GROUP BY year
        ORDER BY year
    """)

def most_controversial_movies(spark, top_n, min_ratings):
    return spark.sql(f"""
        SELECT title, COUNT(rating) AS num_ratings,
               ROUND(AVG(rating), 2) AS avg_rating,
               ROUND(STDDEV(rating), 2) AS stddev_rating
        FROM ratings_with_titles
        GROUP BY title
        HAVING num_ratings > {min_ratings}
        ORDER BY stddev_rating DESC
        LIMIT {top_n}
    """)

def top_movies_per_genre(spark):
    return spark.sql("""
        SELECT genre, title, rating, rank
        FROM (
            SELECT genre, title, rating,
                   ROW_NUMBER() OVER (PARTITION BY genre ORDER BY rating DESC) AS rank
            FROM (
                SELECT title, rating,
                    stack(19,
                        "Action", `Action`,
                        "Adventure", `Adventure`,
                        "Animation", `Animation`,
                        "Children's", `Children's`,
                        "Comedy", `Comedy`,
                        "Crime", `Crime`,
                        "Documentary", `Documentary`,
                        "Drama", `Drama`,
                        "Fantasy", `Fantasy`,
                        "Film-Noir", `Film-Noir`,
                        "Horror", `Horror`,
                        "Musical", `Musical`,
                        "Mystery", `Mystery`,
                        "Romance", `Romance`,
                        "Sci-Fi", `Sci-Fi`,
                        "Thriller", `Thriller`,
                        "War", `War`,
                        "Western", `Western`
                    ) AS (genre, is_genre)
                FROM ratings_with_titles
            ) WHERE is_genre = 1
        ) WHERE rank <= 3
        ORDER BY genre, rank
    """)

def ratings_by_month(spark):
    return spark.sql("""
        SELECT year, month, COUNT(rating) AS num_ratings, ROUND(AVG(rating), 2) AS avg_rating
        FROM ratings_with_titles
        GROUP BY year, month
        ORDER BY year, month
    """)
