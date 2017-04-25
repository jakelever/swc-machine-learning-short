#!/bin/bash
set -euo pipefail

if [[ $# -eq 1 ]]; then
	if [[ "$1" == "--help" ]] ; then
		echo "This tool summaries financial statements. It expects a directory called 'tmp_statements' in the current directory. The statements folder should contain a series of statement files. And it will output the results to the file 'finance_results.txt'"
		exit 0
	else
		echo "ERROR: Unknown argument: $1"
		exit 1
	fi
fi

if [ ! -d tmp_statements/ ]; then
	echo "ERROR: Could not find tmp_statements/ directory"
	exit 1
fi
if [ -f finance_results.txt ]; then
	echo "ERROR: finance_results.txt file already exists"
	exit 1
fi

statementCount=`find tmp_statements/ -name '*_statement.txt' | wc -l`

if [[ $statementCount -eq 0 ]]; then
	echo "ERROR: Couldn't find any statement files"
	exit 1
fi

cat tmp_statements/*_statement.txt |\
awk -F '$' ' { summary[$1] += $2; } END { for (company in summary) print company"\t$ "summary[company]; } ' |\
sort -k2,2nr -t $'$' > finance_results.txt

echo "Summary saved to finance_results.txt using $statementCount statement(s) from the following account(s):"
find tmp_statements/ -name '*_statement.txt' | grep -oP "ACCNO_[0-9]*" | sort -u

