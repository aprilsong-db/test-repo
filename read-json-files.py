# Databricks notebook source
# MAGIC %sql
# MAGIC create temporary view jsonTable
# MAGIC USING json
# MAGIC OPTIONS (path="/test.json")

# COMMAND ----------


