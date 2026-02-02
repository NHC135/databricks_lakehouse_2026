# Config File 

INGESTION_CONFIG = [ 
  # CRM 
  { 
    "source": "crm", 
    "path": "/Volumes/workspace/bronze/source_systems/source_crm/cust_info.csv", 
    "table": "crm_cust_info_raw"  
  }, 
  {
    "source" : "crm",
    "path": "/Volumes/workspace/bronze/source_systems/source_crm/sales_details.csv",
    "table": "crm_sales_details_raw"
  }, 
  { 
    "source" : "crm",
    "path": "/Volumes/workspace/bronze/source_systems/source_crm/prd_info.csv",
    "table": "crm_prd_info_raw"
  },

  # ERP
  {
    "source" : "ERP",
    "path": "/Volumes/workspace/bronze/source_systems/source_erp/CUST_AZ12.csv",
    "table": "erp_CUST_AZ12_raw"
  },
  {
    "source" : "ERP",
    "path": "/Volumes/workspace/bronze/source_systems/source_erp/LOC_A101.csv",
    "table": "erp_LOC_A101_raw"
  },
  {
    "source" : "ERP",
    "path": "/Volumes/workspace/bronze/source_systems/source_erp/PX_CAT_G1V2.csv",
    "table": "erp_PX_CAT_G1V2_raw"
  },
]
