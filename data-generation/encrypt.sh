#!/bin/bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
	echo "USAGE: sh encrypt.sh FILE PASSWORD"
	exit 1
fi

inF=$1
password=$2
outF=tmp

echo "ENCRYPTED" > $outF
echo "$password" | tr '[A-Z]' '[X-ZA-W]' | tr '[a-z]' '[x-za-w]' >> $outF
cat $inF | tr '[A-Z]' '[X-ZA-W]' | tr '[a-z]' '[x-za-w]' >> $outF

mv $outF $inF

echo "Encrypted."

