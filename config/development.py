import os

DEBUG = True
UIPATH_CLIENT_ID = os.getenv('DEVELOPMENT_UIPATH_CLIENT_ID')
UIPATH_CLIENT_SECRET = os.getenv('DEVELOPMENT_UIPATH_CLIENT_SECRET')
UIPATH_ACCESS_TOKEN_URL="https://cloud.uipath.com/identity_/connect/token"
UIPATH_SCOPE="OR.Administration OR.Analytics OR.Assets OR.Audit OR.BackgroundTasks OR.Execution OR.Folders OR.Hypervisor OR.Jobs OR.License OR.Machines OR.ML OR.Monitoring OR.Queues OR.Robots OR.Settings OR.Tasks OR.TestDataQueues OR.TestSetExecutions OR.TestSets OR.TestSetSchedules OR.Users OR.Webhooks PM.Audit PM.Group PM.License PM.RobotAccount PM.Setting PM.User PM.UserLoginAttempt"
UIPATH_CLOUD_BASEURL="https://cloud.uipath.com"
UIPATH_CLOUD_ORGNAME="cprimadotnet"
UIPATH_CLOUD_PARTITION_GLOBAL_ID=""
UIPATH_CLOUD_TENANTS=""
UIPATH_CLOUD_TENANTNAME_CURRENT="homelab23"
UIPATH_CLOUD_TENANTS_DATA=""
UIPATH_CLOUD_MACHINES=""
UIPATH_CLOUD_MACHINES_DATA=""
