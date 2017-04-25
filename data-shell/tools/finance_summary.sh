#!/bin/bash
set -euo pipefail

if [[ $# -eq 1 ]]; then
	if [[ "$1" == "--help" ]] ; then
		echo "This tool summaries financial statements. It expects a directory called 'statements' in the current directory. The statements folder should contain a series of statement files. And it will output the results to the file 'results.tsv"
		exit 0
	else
		echo "ERROR: Unknown argument: $1"
		exit 1
	fi
fi

if [ ! -d statements/ ]; then
	echo "ERROR: Could not find statements/ directory"
	exit 1
fi
if [ -f results.tsv ]; then
	echo "ERROR: results.tsv file already exists"
	exit 1
fi

statementCount=`find statements/ -name '*_statement.txt' | wc -l`

if [[ $statementCount -eq 0 ]]; then
	echo "ERROR: Couldn't find any statement files"
	exit 1
fi

cat statements/*_statement.txt |\
awk -F '$' ' { summary[$1] += $2; } END { for (company in summary) print company"\t$ "summary[company]; } ' |\
sort -k2,2nr -t $'$' > results.tsv

echo "Summary saved to results.tsv using $statementCount statement(s) from the following account(s):"
find statements/ -name '*_statement.txt' | grep -oP "ACCNO_[0-9]*" | sort -u

