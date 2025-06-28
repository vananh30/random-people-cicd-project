from pyspark.sql import SparkSession

def test_spark_connection():
    try:
        spark = SparkSession.builder \
            .appName("TestSparkConnection") \
            .master("spark://spark-master:7077") \
            .getOrCreate()

        print("✅ Spark session created successfully.")

        df = spark.range(1, 10)
        count = df.count()
        print(f"✅ Spark range count: {count}")

        assert count == 9
        print("✅ Test passed: DataFrame count is correct.")

    except Exception as e:
        print("❌ Failed to connect to Spark cluster.")
        print(f"Error: {e}")
    
    finally:
        if 'spark' in locals():
            spark.stop()
            print("ℹ️ Spark session stopped.")

if __name__ == "__main__":
    test_spark_connection()
