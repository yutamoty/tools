@echo off

set INTERFACE="ローカル エリア接続"
echo "SET IPADDR"
set /p IPADDR=""
echo "SET NETMASK"
set /p MASK=""
echo "SET GW"
set /p GW=""

echo "次の情報で設定します。"

echo ***********************
echo IF  =%INTERFACE%
echo ip  =%IPADDR
echo MASK=%MASK%
echo GW  =%GW%
echo ***********************
echo .
pause

netsh interface ipv4 set address name=%INTERFACE% static %IPADDR% %MASK% %GW% 1

:end
