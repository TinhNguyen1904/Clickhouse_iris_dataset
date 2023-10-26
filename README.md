PREPARATION STEPS:
    Install postgreSQL locally
    Sign up for an account on clickhouse cloud
    To run python scripts, install the necessary libraries:
        pip install Flask-SQLAlchemy
        pip install psycopg2-binary
        pip install sql
        pip install pandahouse
        pip install numpy
        pip install pandas
        pip install matplotlib
        pip install seaborn
To import data into postgreSQL and clickhouse, you need to change the connection configuration in the code to your required configuration

PROJECT IMPLEMENTATION STEPS:
    Task 1: 
    Choose an arbitrary dataset - here select the iris dataset
    Import data using python
    iris_data_with_task1_task2.ipynb in src folder

    Task 2:
    Clean and transform data
    Create statistical parameters:
        Thereby, it can be seen that there are three types of flowers with an equal number of 100
        obervation:
        1. petal.lenght and petal.width are the most useful features to identify various flower types.
        2. While Sentosa can be easily identified(linearly seperable), Virnica and Versicolor have some overlap(almost linearly separable)
        3. We can find "lines" and "if-else" conditions to build a simple model to classify the flower types.
    Task 3:
        Store SQL schema in postgreSQL:
        * table name: data_iris
        sepal_length: length of sepals
        sepal_width: width of sepals
        petal_length: length of petals
        petal_width: width of petals
        class: classification of flowers

        SQL query: SELECT * FROM data_iris

    Task 4: Data Transfer with Airflow
    File: dag_import_data_clickhouse.py in src folder

    Task 5:
    Query data with ClickHouse
    Assumptions:
    separate_length: X
    petal_length: Y
    class: Z
    1. How many unique values are in variable X?
    SELECT sepal_length, COUNT(sepal_length) as count
    FROM data_iris
    GROUP BY separate_length
    HAVING count = 1

    2. What is the average of variable Y grouped by variable Z?
    SELECT class, AVG(petal_length) as avg
    FROM data_iris
    GROUP BY class