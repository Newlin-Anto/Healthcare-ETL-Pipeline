from pyspark.sql import functions as F
from pyspark.sql.functions import sum, avg, count


def process_data(transform_df):

    process_df = transform_df.withColumn(
        "Stay Duration",
        F.datediff(
            F.col("Discharge Date"),
            F.col("Date of Admission")
        )
    )

    process_df = process_df.withColumn(
        "Age Group",
        F.when(F.col("Age") <= 18, "Child")
        .when(F.col("Age") <= 60, "Adult")
        .otherwise("Senior")
    )

    hospital_summary_df = process_df.groupBy("Hospital").agg(
        count("Name").alias("Patient Count"),
        sum("Billing Amount").alias("Total Billing"),
        avg("Billing Amount").alias("Average Billing"),
        avg("Stay Duration").alias("Average Stay")
    )

    insurance_summary_df = process_df.groupBy(
        "Insurance Provider"
    ).agg(
        count("Name").alias("Patient Count"),
        sum("Billing Amount").alias("Total Billing"),
        avg("Billing Amount").alias("Average Billing")
    )

    return process_df, hospital_summary_df, insurance_summary_df
