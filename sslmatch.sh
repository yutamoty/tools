#/usr/bin/env bash


### file check
if [ -z "${1}" ] ;
then
    echo "Usage: $0 <crt or key> <crt or key>"
    exit 1
else
    if [ -z "${2}" ] ;
    then
        echo "Usage: $0 <crt or key> <crt or key>"
        exit 1
    else
        if [ -n "${3}" ] ;
        then
            echo "Usage: $0 <crt or key> <crt or key>"
            exit 1
        fi
    fi
fi

for LIST in "$@"
do
    case ${LIST} in
        *".crt" ) CRT=${LIST} ;;
        *".key" ) KEY=${LIST} ;;
        * ) echo "key = .key / crt = .crt" ;;
    esac
done

if [ -z "${CRT}" ] ;
then
    echo "no CRT"
    exit 1
else
    if [ -z "${KEY}" ] ;
    then
        echo "no KEY"
        exit 1
    fi
fi

if [ ! -f "${CRT}" ]
then
    echo "no CRT file"
    exit 1
else
    if [ ! -f "${KEY}" ] ;
    then
        echo "no KEY file"
        exit 1
    fi
fi

### process

MD5CRT=$(openssl x509 -noout -modulus -in ${CRT} | openssl md5)
MD5KEY=$(openssl rsa -noout -modulus -in ${KEY} | openssl md5)

if [ "${MD5CRT}" == "${MD5KEY}" ] ;
then
    echo "openssl x509 -noout -modulus -in ${CRT} | openssl md5"
    echo ${MD5CRT}
    echo "openssl rsa -noout -modulus -in ${KEY} | openssl md5"
    echo ${MD5KEY}
    echo ""
    echo "match"
else
    echo "openssl x509 -noout -modulus -in ${CRT} | openssl md5"
    echo ${MD5CRT}
    echo "openssl rsa -noout -modulus -in ${KEY} | openssl md5"
    echo ${MD5KEY}
    echo ""
    echo "no match"
fi
