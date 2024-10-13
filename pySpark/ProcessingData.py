#!/usr/bin/env python
# coding: utf-8

# # Import

# In[15]:


# !pip install pymongo
# !pip install pyspark
# !pip install pandas numpy


# In[16]:


from pymongo import MongoClient


# In[16]:





# ## Connect database

# In[17]:


client = MongoClient()
client = MongoClient("localhost", 27017)
#Chạy trên jupyter notebook thì bỏ comment dòng dưới
client = MongoClient('mongodb://mymongodb:27017')


# In[18]:


db = client.dbmycrawler
collection = db.tblphongtro123
print(collection.find_one())


# ## Got Data

# In[ ]:


data = [i for i in collection.find()]


# In[ ]:


for i in range(len(data)):
    data[i].pop('_id', None)


# # Init PySpark
# 

# In[ ]:


import os
import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable


# In[ ]:


from pyspark.sql import SparkSession

spark = SparkSession.builder.master("local[*]").getOrCreate()
#spark = SparkSession.builder.remote("sc://localhost:15002").getOrCreate()


# In[ ]:


data = spark.createDataFrame(data)


# # EDA

# ## Cleaning

# In[ ]:


from pyspark.sql.functions import regexp_replace, col

data = data.withColumn("acreage", regexp_replace(col("acreage"), "m", "").cast("float"))
data = data.withColumn("address", regexp_replace(col("address"), "Địa chỉ: ", ""))


# In[ ]:


from pyspark.sql.functions import regexp_replace, col, when

data = data.withColumn(
    "price",
    when(
        col("price").contains("triệu/tháng"),
        regexp_replace(col("price"), "triệu/tháng", "")
        .cast("float") * 10000000
    ).otherwise(col("price"))
)

data = data.withColumn(
    "price",
    when(
        col("price").contains("đồng/tháng"),
        regexp_replace(col("price"), "đồng/tháng", "")
        .cast("float")
    ).otherwise(col("price"))
)


# In[ ]:


new_column_names = [col_name.replace("_", " ").title() for col_name in data.columns]

data = data.toDF(*new_column_names)


# In[ ]:


data.show()


# ## Data modeling

# In[ ]:


type(data)

