def extract_data(spark):
    raw_df = spark.read.csv(
        "hdfs://localhost:9000/healthcare/raw/healthcare_dataset.csv",
        header=True,
        inferSchema=True
    )

    return raw_df
