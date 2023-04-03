#!/bin/bash

# Anmol Kapoor

# In this file you will find an example of how to format a CSV file's headers into an
# easy-to-understand markdown-supported list.
# Usage:
#   ./mdHeader.sh [CSV File]
# Example:
#   ./mdHeader.sh iris.csv

echo "\`$1\` has the following features:"
echo -n ' - `'
cat $1 | head -n 1 | sed 's/,/\n - `/g' | sed 's/$/`/g'
