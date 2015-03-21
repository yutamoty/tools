#/usr/bin/env bash

DOMAIN='example.com'
PASSWD='hogehoge'
HOST='ddns'

DIR=$(dirname $0)

curl -s http://dyn.value-domain.com/cgi-bin/dyn.fcg?ip -o "${DIR}/current_ip.txt" -w '%{http_code}' > "${DIR}/status.txt"

status=$(cat "${DIR}/status.txt")

echo ${status}
if [ '200' != "${status}" ] ; then
    echo "$(date +"%Y/%m/%d-%H:%M") http status error statuscode:${status}" >> "${DIR}/ng_log.txt"
    exit 1
fi

prev=$(cat "${DIR}/prev_ip.txt")
current=$(cat "${DIR}/current_ip.txt")

echo ${prev}
echo ${current}

if [ "${prev}" = "${current}" ] ; then
    echo "no change"
    exit 0
fi

cat "${DIR}/current_ip.txt" > "${DIR}/prev_ip.txt"

wget -O - "http://dyn.value-domain.com/cgi-bin/dyn.fcg?d=${DOMAIN}&p=${PASSWD}&h=${HOST}&i=${current}"

exit 0
