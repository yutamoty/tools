#/usr/bin/env bash

DOMAIN='example.com'
PASSWD='hogehoge'
HOST='*'

curl -s http://dyn.value-domain.com/cgi-bin/dyn.fcg?ip -o current_ip.txt -w '%{http_code}' > status.txt

status=$(cat status.txt)

echo ${status}
if [ '200' != "${status}" ] ; then
    echo "$(date +"%Y/%m/%d-%H:%M") http status error statuscode:${status}" >> ng_log.txt
    exit 1
fi

prev=$(cat prev_ip.txt)
current=$(cat current_ip.txt)

echo ${prev}
echo ${current}

if [ "${prev}" = "${current}" ] ; then
    echo "no change"
    exit 0
fi

cat current_ip.txt > prev_ip.txt

wget -O - "http://dyn.value-domain.com/cgi-bin/dyn.fcg?d=${DOMAIN}&p=${PASSWD}&h=${HOST}&i=${current}"

exit 0
