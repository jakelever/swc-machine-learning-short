#!/bin/bash
set -euo pipefail

function usage {
	echo "USAGE: sh decrypt.sh PASSWORD FILE"
	echo
	echo "PASSWORD: The password used to encrypt the file"
	echo "FILE: The file to decrypt"
	echo
	echo "There is a test file in the toolset. Try decrypting it. The password is SECRET."
	exit 1
}
if [[ $# -ne 2 ]]; then
	usage
fi

password=$1
inF=$2

decryptedPassword=`head -n 2 $inF | tail -n 1 | tr '[X-ZA-W]' '[A-Z]' | tr '[x-za-w]' '[a-z]'`
if [[ "$password" != "$decryptedPassword" ]]; then
	echo "Password is incorrect"
	exit 1
fi

cat $inF | tail -n +3 | tr '[X-ZA-W]' '[A-Z]' | tr '[x-za-w]' '[a-z]'

