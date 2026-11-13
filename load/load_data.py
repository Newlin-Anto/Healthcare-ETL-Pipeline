def load_data(
    process_df,
    hospital_summary_df,
    insurance_summary_df
):

    process_df.write.mode("overwrite").parquet(
        "hdfs://localhost:9000/healthcare/processed/patient_data"
    )

    hospital_summary_df.write.mode("overwrite").parquet(
        "hdfs://localhost:9000/healthcare/processed/hospital_summary"
    )

    insurance_summary_df.write.mode("overwrite").parquet(
        "hdfs://localhost:9000/healthcare/processed/insurance_summary"
    )
