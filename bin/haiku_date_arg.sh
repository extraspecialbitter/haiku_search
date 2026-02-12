#!/bin/bash

# Function to validate date format (dd-Mon-YYYY, e.g., 15-Dec-2025)
validate_date() {
    local input="$1"
    
    # Check if date matches the expected format (accept both single and double-digit days)
    if [[ ! "$input" =~ ^[0-9]{1,2}-[A-Z][a-z]{2}-[0-9]{4}$ ]]; then
        echo "Error: Invalid format. Please use format: d-Mon-YYYY or dd-Mon-YYYY (e.g., 1-Jan-2025 or 15-Dec-2025)"
        return 1
    fi
    
    # Try to parse the date to ensure it's valid
    if ! date -d "$input" +%s >/dev/null 2>&1; then
        echo "Error: Invalid date. Please enter a valid date."
        return 1
    fi
    
    return 0
}

# Check if a date argument was provided
if [[ $# -eq 0 ]]; then
    echo "Usage: $0 <date>"
    echo "Format: d-Mon-YYYY or dd-Mon-YYYY (e.g., 1-Jan-2025 or 15-Dec-2025)"
    exit 1
fi

day_month_and_year="$1"

# Validate the date
if ! validate_date "$day_month_and_year"; then
    exit 1
fi

# Extract components from the validated date
day_and_month=$(date -d "$day_month_and_year" +%_d-%b)
this_year=$(date -d "$day_month_and_year" +%Y)

# Run the haiku search commands
day_tally=$(${HOME}/git/haiku_search/bin/print_archive_table.py ${this_year} | grep "${day_and_month}")
day_count=$(${HOME}/git/haiku_search/bin/print_archive_table.py ${this_year} | grep -c "${day_and_month}")

# Display results
echo " "
echo "${day_tally}"
echo " "
echo "${day_count} haiku written on ${day_month_and_year}"