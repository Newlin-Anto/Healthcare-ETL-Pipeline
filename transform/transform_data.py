from pyspark.sql import functions as F


def transform_data(raw_df):

    clean_df = raw_df.distinct()

    clean_df.count()

    duplicate_df = raw_df.groupBy(raw_df.columns) \
        .count() \
        .filter(F.col("count") > 1)

    duplicate_df.show()
    duplicate_df.count()

    clean_df.select("Gender").distinct().show()
    clean_df.select("Blood Type").distinct().show()
    clean_df.select("Medical Condition").distinct().show()
    clean_df.select("Admission Type").distinct().show()
    clean_df.select("Test Results").distinct().show()
    clean_df.select("Insurance Provider").distinct().show()
    clean_df.select("Medication").distinct().show()

    clean_df.select(
        F.min("Age").alias("min_age"),
        F.max("Age").alias("max_age")
    ).show()

    clean_df.filter(
        F.col("Billing Amount") < 1
    ).show()

    clean_df.filter(
        F.col("Date of Admission") > F.col("Discharge Date")
    ).show()

    clean_df = raw_df.distinct()

    clean_df = clean_df.filter(
        F.col("Billing Amount") > 0
    )

    clean_df = clean_df.withColumn(
        "Name",
        F.initcap(F.col("Name"))
    )

    transform_df = clean_df

    return transform_df
