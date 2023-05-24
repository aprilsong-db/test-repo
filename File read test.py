# Databricks notebook source
# MAGIC %ls

# COMMAND ----------

# MAGIC %pwd

# COMMAND ----------


import os

file_content = open("/Workspace/Repos/april.song@databricks.com/test-repo/read-json-files")
temp = file_content.read()
file_content.close()
temp 

# COMMAND ----------

file_content = open("/Workspace/Repos/april.song@databricks.com/test-repo/notebooks/a.py")
temp = file_content.read()
file_content.close()
print(temp)



# COMMAND ----------

file_content = open("/Workspace/Repos/april.song@databricks.com/test-repo/test.json")
temp = file_content.read()
file_content.close()
print(temp)

# COMMAND ----------

file_content = open("/Workspace/Repos/april.song@databricks.com/test-repo/notebooks/b.sql")
temp = file_content.read()
file_content.close()
print(temp)

# COMMAND ----------

file_content = open("/Workspace/Repos/april.song@databricks.com/test-repo/notebooks/notebook")
temp = file_content.read()
file_content.close()
print(temp)

# COMMAND ----------


