# Databricks Lakehouse Project 2026  

This repository contains a complete, real-world Data Lakehouse implementation built on Databricks, including datasets, notebooks, SQL examples, and exercises. Everything here is designed to building an understanding on how modern data teams use Databricks in practice, from data ingestion and transformation to analytics-ready data products.

# Architecture
This project follows the Medallion Architecture:    
  
<img width="724" height="799" alt="data model" src="https://github.com/user-attachments/assets/4fd0a80e-a4c5-4f8c-beef-d54f4681e159" />

## Bronze Layer
Raw data ingestion
Schema inference and storage as Delta tables
## Silver Layer
Data cleaning and standardization
Type casting and validation
## Gold Layer
Dimensional Data Model (Business Transformation)
Ready for BI and analysis    
  
<img width="767" height="748" alt="Data Model Star Schema" src="https://github.com/user-attachments/assets/1651552a-693c-45d9-a9f2-3c18bc31650a" />

## Technologies Used
Databricks  
Apache Spark  
PySpark  
Spark SQL  
Delta Lake  
Unity Catalog  

## License
This project is licensed under the MIT License. You are free to use, modify, and share this project with proper attribution.
