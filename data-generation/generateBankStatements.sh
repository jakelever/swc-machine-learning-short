#!/bin/bash
set -euxo pipefail

mkdir bank_statements

SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

noOfAccounts=40

for accNo in `cat /dev/urandom | tr -dc '0-9' | fold -w 8 | head -n $noOfAccounts | sort`
do
#seq 10 | xargs -I NUM printf "%02d\n" NUM | xargs -I NUM python $SCRIPTDIR/finance_generator.py --outFile bank_statements/ACCNO_$accNo\_statement_NUM.txt
	python $SCRIPTDIR/finance_generator.py --outFile bank_statements/ACCNO_$accNo\_statement.txt
done

