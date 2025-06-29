

# Random People End-to-End CI/CD Data Pipeline

## 📌 Overview

This project is a complete data pipeline that fetches random user data from an external API, stores it in AWS S3, processes it with Spark, and loads it into a PostgreSQL database. The workflow is orchestrated with Apache Airflow, and the infrastructure is managed using Terraform. CI/CD is handled via GitHub Actions and Docker Compose.

---

## ✨ Features

* **API Data Ingestion:** Fetches random user data from [randomuser.me](https://randomuser.me/).
* **AWS S3 Storage:** Stores raw data in an S3 bucket.
* **Spark Processing:** Reads and flattens JSON data using PySpark.
* **PostgreSQL Loading:** Loads processed data into normalized tables.
* **Airflow Orchestration:** Manages the ETL workflow as a DAG.
* **Terraform IaC:** Provisions AWS resources (S3 bucket).
* **CI/CD:** Automated build, test, and deployment pipeline.
* **Unit Tests:** Pytest-based tests for ETL components.

---

## 📁 Project Structure

```
CICD/
├── airflow/
│   └── dags/
│       └── dag.py
├── src/
│   ├── get_data.py
│   ├── upload_to_postgres.py
│   └── test_spark_conn.py
├── tests/
│   ├── get_data_test.py
│   └── upload_to_postgres_test.py
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
├── docker-compose.yaml
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🚀 Getting Started

### ✅ Prerequisites

* Docker & Docker Compose
* Terraform
* AWS account & credentials

### ⚙️ Setup

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd CICD
   ```

2. **Configure Environment Variables**

   Create a `.env` file in the root directory with your AWS and database credentials.

3. **Provision AWS Resources**

   ```bash
   cd terraform
   terraform init
   terraform apply
   ```

4. **Build and Start Services**

   ```bash
   docker compose up --build
   ```

5. **Access Services**

   * **Airflow UI:** [http://localhost:8080](http://localhost:8080)
   * **Jupyter:** [http://localhost:8888](http://localhost:8888)
   * **Spark UI:** [http://localhost:18080](http://localhost:18080)
   * **PostgreSQL:** `localhost:5432`

6. **Run the Pipeline**

   * Trigger the DAG in Airflow UI (`random_name_api_dag`).
   * Or run scripts manually:

     ```bash
     docker compose exec airflow-webserver python /opt/airflow/src/get_data.py
     docker compose exec airflow-webserver python /opt/airflow/src/upload_to_postgres.py
     ```

7. **Run Tests**

   ```bash
   docker compose exec airflow-webserver pytest /opt/airflow/tests
   ```

---

## 🧪 Tests

This project uses **Pytest** and **unittest.mock** for unit and integration tests.

### 🔍 Test Summary

| Test Function                   | Purpose                                                                       |
| ------------------------------- | ----------------------------------------------------------------------------- |
| `test_define_schema`            | Verifies schema definition returns a Spark `StructType` with expected fields. |
| `test_get_data_from_s3`         | Mocks AWS S3 response to test successful data retrieval.                      |
| `test_connect_postgres_success` | Mocks PostgreSQL connection to ensure connectivity logic works.               |
| `test_create_flat_dataframe`    | Checks DataFrame creation and flattening logic with sample data.              |
| `test_insert_data_to_postgres`  | Tests data insertion logic into PostgreSQL using mocked connections.          |
| `test_load_to_postgres`         | End-to-end mock test for the full ETL process function.                       |

✅ **Run locally:**

```bash
docker compose exec airflow-webserver pytest /opt/airflow/tests
```

---

## ⚡ CI/CD

* **GitHub Actions** workflow:

  * Runs on pull requests to `main`.
  * Builds Docker images.
  * Runs all tests inside Docker containers.
  * Tears down services after testing.

---

## 📄 License

MIT License

---

🔒 **Note:** Do not commit your `.env` or AWS credentials to version control.


