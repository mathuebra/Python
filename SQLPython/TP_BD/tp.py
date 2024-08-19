import oracledb

username = "ECLBDIT210"
password = "Matjony@2000"
dsn = "(DESCRIPTION=(RETRY_COUNT=20)(RETRY_DELAY=3)(ADDRESS=(PROTOCOL=TCPS)(PORT=1522)(HOST=adb.sa-saopaulo-1.oraclecloud.com))(CONNECT_DATA=(SERVICE_NAME=f55grwkwpyhckzx_bdec_high.adb.oraclecloud.com))(SECURITY=(SSL_SERVER_DN_MATCH=YES)))"

connection = oracledb.connect(
    user=username,
    password=password,
    dsn=dsn
)

