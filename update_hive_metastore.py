#!/usr/bin/python

from cm_api.api_client import ApiResource
import datetime
import time
import requests
import smtplib

# CM Crenditials
cmHost = "CM_HOSTNAME"
cmUsername = "CM_USER"
cmPassword = "CM_PASSWORD"


cluster_name = { 'cluster_name': "CLUSTER_NAME" }

# Hive MetastoreDB details
hive_service_config = {
  'hive_metastore_database_host': '$metastore_db_host',
  'hive_metastore_database_name': '$metastore_db_name',
  'hive_metastore_database_user': '$metastore_user',
  'hive_metastore_database_password': '$metastore_password',
  'hive_metastore_database_port': 3306,
  'hive_metastore_database_type': 'mysql'
}

api = ApiResource(cmHost, username=cmUsername, password=cmPassword)
cluster =  api.get_cluster(cluster_name['cluster_name'])


print("Updating Hive MetaStore DB Name, Password")
for service in cluster.get_all_services():
    if service.type == "HIVE":
       hive = service
       #hive.get_role_types()
       #hive.get_config()
       hive.update_config({'hive_metastore_database_host': hive_service_config['hive_metastore_database_host']})
       hive.update_config({'hive_metastore_database_name': hive_service_config['hive_metastore_database_name']})
       hive.update_config({'hive_metastore_database_user': hive_service_config['hive_metastore_database_user']})
       hive.update_config({'hive_metastore_database_password': hive_service_config['hive_metastore_database_password']})
       hive.update_config({'hive_metastore_database_port': hive_service_config['hive_metastore_database_port']})
       hive.update_config({'hive_metastore_database_type': hive_service_config['hive_metastore_database_type']})


print("Updating Hive MetaStore DB Name, Password - Complete")
