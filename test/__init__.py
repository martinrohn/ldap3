from os import environ

environ["SERVER"]="SLAPD"
environ["STRATEGY"]="RESTARTABLE"
environ["USERDOMAIN"]="TRAVIS"
environ["LAZY"]="FALSE"
environ["DECODER"]="INTERNAL"
environ["CHECK_NAMES"]="TRUE"