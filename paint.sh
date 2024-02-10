#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <X> <run_count>"
    exit 1
fi

X=$1
run_count=$2
output_file="output_$X.txt"

for ((i=1; i<=$run_count; i++)); do
    echo Run $i
    python paintwars.py $X True 2 | grep ' winner="'  >> "$output_file"
done

for ((i=1; i<=$run_count; i++)); do
    echo Run $i
    python paintwars.py $X False 2 | grep ' winner="'  >> "$output_file"
done

echo "Output saved to $output_file"

wins=$(grep -o "EGE" $output_file | wc -l)
losses=$(grep -o "Professor X" $output_file | wc -l)
draws=$(grep -o "nobody" $output_file | wc -l)

total=$((wins+losses+draws))

echo "Wins: $wins"
echo "Losses: $losses"
echo "Draws: $draws"
echo "-----------------"
echo "Total: $total"

