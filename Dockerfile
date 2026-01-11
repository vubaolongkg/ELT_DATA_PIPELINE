# Sử dụng base image chính chủ của Airflow
FROM apache/airflow:2.7.1

# Chuyển sang user root để cài đặt các gói hệ thống (nếu cần)
USER root
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean

# Chuyển lại về user airflow để cài đặt thư viện Python
USER airflow

# Copy file requirements vào trong container
COPY requirements.txt .

# Cài đặt các thư viện
RUN pip install --no-cache-dir -r requirements.txt
