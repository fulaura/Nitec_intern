# 🎬 MovieLens 100K Analysis with Apache Spark

This project analyzes the [MovieLens 100K dataset](https://grouplens.org/datasets/movielens/100k/) using PySpark and Spark SQL. It performs various analytical tasks such as identifying top-rated and most controversial movies, genre analysis, and trends over time.

---

## 🚀 Features

- Top N movies by average rating
- Average rating by genre (stacked transformation)
- Yearly and monthly rating trends
- Most controversial movies (highest rating std deviation)
- Top 3 movies per genre (window functions)

---

## 📦 Technologies

- Python 3.10+
- Apache Spark 3.x
- PySpark SQL
- Docker

---

## 🛠️ Setup

### 🔁 Clone the repository

```bash
git clone https://github.com/yourusername/spark-movielens.git
cd spark-movielens

## Build the Docker image:
docker build -t spark-movielens .

## Run the container (PowerShell):
docker run -it -v ${PWD}/data:/app/data -v ${PWD}/output:/app/output spark-movielens

