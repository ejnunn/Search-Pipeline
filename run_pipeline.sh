# Setup
corpus=$(ls data/state_union/*.txt)  # Expanding the glob pattern
mkdir -p output # Ensure the output directory exists

# Run the Term Count Job
echo "Running the Term Count Job"
for file in $corpus; do
    export map_input_file="$file"
    cat "$file" | python3 term_count/mapper.py | sort | python3 term_count/reducer.py
done > output/term_counts.txt

# Run the Total Term Count Job
echo "Running the Total Term Count Job"
for file in $corpus; do
    export map_input_file="$file"
    cat "$file" | python3 total_term_count/mapper.py | sort | python3 total_term_count/reducer.py
done > output/total_term_counts.txt

# Run the TF Job
echo "Running the Term Frequency (TF) Job"
cat output/term_counts.txt | python3 tf/mapper.py | sort | python3 tf/reducer.py > output/tf.txt


# Run the DF Job


# Compute TF-IDF
