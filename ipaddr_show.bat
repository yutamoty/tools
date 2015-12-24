@echo off

echo "ローカルエリア接続の情報取得"

echo ""

netsh interface dump | findstr "ローカル"

pause
