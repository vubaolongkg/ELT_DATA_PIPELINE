🚀 End-to-End ELT Data Pipeline with Airflow, dbt, and Postgres
📖 Overview
This project demonstrates a production-ready ELT (Extract, Load, Transform) pipeline using the Modern Data Stack. Fully containerized with Docker, it extracts e-commerce product data from a public API, loads it into PostgreSQL Data Warehouse, transforms it with dbt into a dimensional model, and powers analytics in Power BI.

🏗️ Architecture
text
graph LR
    A[Fake Store API] -->|1. Extract| B[Postgres<br/>Raw Layer]
    B -->|2. Transform| C[Postgres<br/>Serving Layer]
    C -->|3. Visualize| D[Power BI Dashboard]
    
    subgraph "Docker Containers"
        E[Apache Airflow 2.7.1] -->|Orchestrates| F[ingest_products.py]
        E -->|Triggers| G[dbt run]
    end
🛠️ Tech Stack
Orchestration: Apache Airflow 2.7.1

Ingestion: Python (Pandas, SQLAlchemy)

Data Warehouse: PostgreSQL 13

Transformation: dbt Core 1.5.0

Visualization: Microsoft Power BI

Infrastructure: Docker & Docker Compose

✨ Key Features
🔄 Fully Automated: Airflow schedules and monitors the complete ELT flow

🐳 Containerized: Infrastructure-as-Code with docker-compose

🔧 Modular Transformations: dbt handles SQL models, tests, and docs

📊 Dimensional Modeling: Raw JSON → Clean fact/dimension tables

🚀 Production Ready: Error handling, logging, and monitoring

📂 Project Structure
text
.
├── dags/                   # Airflow DAGs
│   └── elt_pipeline.py
├── dbt_project/            # dbt transformations
│   ├── models/
│   │   └── dim_products.sql
│   ├── dbt_project.yml
│   └── profiles.yml
├── scripts/                # Python ingestion
│   └── ingest_products.py
├── docker-compose.yaml     # Infrastructure
├── Dockerfile              # Custom Airflow + dbt image
└── requirements.txt
🚀 Quick Start
Prerequisites
Docker Desktop

Power BI Desktop (optional, for visualization)

Step 1: Clone & Build
bash
git clone https://github.com/YOUR_USERNAME/elt-airflow-dbt-pipeline.git
cd elt-airflow-dbt-pipeline
docker-compose build
Step 2: Launch Pipeline
bash
docker-compose up -d
Wait ~30s for services to initialize

Step 3: Access Airflow
URL: http://localhost:8080

Login: airflow / airflow

Step 4: Run Pipeline
Find elt_pipeline_v1 DAG

Toggle Unpause

Click Trigger DAG ▶️

Monitor in Graph View

Step 5: Connect Power BI
text
Server: localhost:5432
Database: airflow
User: airflow
Password: airflow
Table: dim_products
📊 Data Flow
text
1. EXTRACT: FakeStore API → raw_products (JSON flattened)
2. LOAD:   PostgreSQL raw layer
3. TRANSFORM: dbt → dim_products (clean, typed, business-ready)
4. ANALYZE: Power BI dashboards
📸 Screenshots
✅ Airflow Pipeline Success
📈 Power BI Dashboard
