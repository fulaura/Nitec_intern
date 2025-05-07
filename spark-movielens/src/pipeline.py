from src.views import create_temp_views
from src import queries

def run_pipeline(spark, ratings_df, movies_df, top_n, min_ratings):
    create_temp_views(spark, ratings_df, movies_df)

    print(f"\n=== Top {top_n} Rated Movies (min {min_ratings} ratings) ===")
    queries.top_rated_movies(spark, top_n, min_ratings).show(truncate=False)

    print("\n=== Average Rating by Genre ===")
    queries.average_rating_by_genre(spark).show(truncate=False)

    print("\n=== Ratings by Year ===")
    queries.ratings_by_year(spark).show(truncate=False)

    print(f"\n=== Most Controversial Movies (min {min_ratings} ratings) ===")
    queries.most_controversial_movies(spark, top_n, min_ratings).show(truncate=False)

    print("\n=== Top 3 Movies per Genre ===")
    queries.top_movies_per_genre(spark).show(truncate=False)

    print("\n=== Ratings by Month ===")
    queries.ratings_by_month(spark).show(truncate=False)
