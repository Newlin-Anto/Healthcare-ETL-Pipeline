from pyspark.sql import SparkSession

from extract.extract_data import extract_data
from transform.transform_data import transform_data
from process.process_data import process_data
from load.load_data import load_data


spark = SparkSession.builder \
    .appName("Healthcare ETL Pipeline") \
    .getOrCreate()


raw_df = extract_data(spark)

transform_df = transform_data(raw_df)

process_df, hospital_summary_df, insurance_summary_df = process_data(
    transform_df
)

load_data(
    process_df,
    hospital_summary_df,
    insurance_summary_df
)

print("Healthcare ETL Pipeline Completed Successfully!")

spark.stop()
