#!/bin/bash
# Generate monthly report from transaction data
# Usage: ./generate_report.sh [month] [year]

MONTH=${1:-$(date +%m)}
YEAR=${2:-$(date +%Y)}

echo "Generating report for $YEAR-$MONTH..."

# Count transactions
COUNT=$(grep "$YEAR-$MONTH" data/sales-data-2024.csv | wc -l)
echo "Transactions found: $COUNT"

# Calculate total
TOTAL=$(grep "$YEAR-$MONTH" data/sales-data-2024.csv | awk -F',' '{sum += $3} END {printf "%.2f", sum}')
echo "Total revenue: $TOTAL"

echo "Report saved to reports/monthly-$YEAR-$MONTH.md"
