# Databricks notebook source
# MAGIC %md
# MAGIC ## Current Context Notebook
# MAGIC > Use this to programmatically access information about your current environment.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Current User
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Current User
# Get the current user name.
userName = dbutils.entry_point.getDbutils().notebook().getContext().userName().get()
print("Current User Name: ", userName)

userId = dbutils.entry_point.getDbutils().notebook().getContext().tags().get("userId").get()
print("Current User Id: ", userId)

# COMMAND ----------

# DBTITLE 1,Current User Agent
userAgent = dbutils.entry_point.getDbutils().notebook().getContext().tags().get("userAgent").get()
print("Current User Agent: ", userAgent)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Current Workspace
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,UC Enabled
# Is UC Enabled
ucEnabled = spark.conf.get("spark.databricks.unityCatalog.enabled")
print("Unity Catalog Enabled: ", ucEnabled)

# Current Metastore
currentMetastore = spark.sql("SELECT CURRENT_METASTORE()").first()[0]
print("Current metastore: ", currentMetastore)

# COMMAND ----------

# DBTITLE 1,Workspace Info
# Get the current workspace Id using dbutils.
workspaceId = dbutils.entry_point.getDbutils().notebook().getContext().workspaceId().get()
print("Workspace ID: ", workspaceId)

# Get the workspace URL with spark conf.
workspaceUrl = spark.conf.get("spark.databricks.workspaceUrl")
print("Workspace URL: ", workspaceUrl)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Current Cluster
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Cloud Info
# Get the current region
region = spark.conf.get("spark.databricks.clusterUsageTags.region")
print("Region: ", region)

# COMMAND ----------

# DBTITLE 1,Cluster Info
# High level cluster information

clusterName = spark.conf.get("spark.databricks.clusterUsageTags.clusterName")
print("Cluster Name: ", clusterName)

clusterId = spark.conf.get("spark.databricks.clusterUsageTags.clusterId")
print("Cluster ID: ", clusterId)

databricks_runtime_version = spark.conf.get("spark.databricks.clusterUsageTags.sparkVersion")
print("DBR version: ", databricks_runtime_version)

clusterMetastoreAccessType = spark.conf.get("spark.databricks.clusterUsageTags.clusterMetastoreAccessType")
print("Cluster Metastore Access Type: ", clusterMetastoreAccessType)

clusterUnityCatalogMode = spark.conf.get("spark.databricks.clusterUsageTags.clusterUnityCatalogMode")
print("Cluster Unity Catalog Access Mode: ", clusterUnityCatalogMode)

isSingleUserCluster = spark.conf.get("spark.databricks.clusterUsageTags.isSingleUserCluster")
print("Is Single User Cluster: ", isSingleUserCluster)

privateLinkEnabled = spark.conf.get("spark.databricks.clusterUsageTags.privateLinkEnabled")
print("Private Link Enabled: ", privateLinkEnabled)

clusterNumCustomTags = spark.conf.get("spark.databricks.clusterUsageTags.clusterNumCustomTags")
print("Number Custom Tags: ", clusterNumCustomTags)

clusterSku = spark.conf.get("spark.databricks.clusterUsageTags.clusterSku")
print("Cluster SKU: ", clusterSku)

# COMMAND ----------

# DBTITLE 1,Driver Info
driverNodeType = spark.conf.get("spark.databricks.clusterUsageTags.driverNodeType")
print("Driver Node Type: ", driverNodeType)

driverInstanceId = spark.conf.get("spark.databricks.clusterUsageTags.driverInstanceId")
print("Driver Instance ID: ", driverInstanceId)

# COMMAND ----------

# DBTITLE 1,Worker Info
clusterWorkers = spark.conf.get("spark.databricks.clusterUsageTags.clusterWorkers")
print("Cluster Workers: ", clusterWorkers)

clusterMinWorkers = spark.conf.get("spark.databricks.clusterUsageTags.clusterMinWorkers")
print("Cluster Min Workers: ", clusterMinWorkers)

clusterMaxWorkers = spark.conf.get("spark.databricks.clusterUsageTags.clusterMaxWorkers")
print("Cluster Max Workers: ", clusterMaxWorkers)

clusterNodeType = spark.conf.get("spark.databricks.clusterUsageTags.clusterNodeType")
print("Cluster Node Type: ", clusterNodeType)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Current Notebook
# MAGIC ---

# COMMAND ----------

# DBTITLE 1,Current Notebook Info
# Get the current notebook ID.
notebook_id = dbutils.entry_point.getDbutils().notebook().getContext().notebookId().get()
print("Notebook ID: ", notebook_id)

# Get the current notebook path.
notebook_path = dbutils.entry_point.getDbutils().notebook().getContext().notebookPath().get()
print("Notebook path: ", notebook_path)
