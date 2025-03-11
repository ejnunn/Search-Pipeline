# Distributed Scalable Search Pipeline using Hadoop MapReduce
Hadoop MapReduce job for Term Frequency-Inverse Document Frequency ([TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)).

Index a corpus of text documents and calculate the TF-IDF values for each term. Query to search for relevancy of key words within the text corpus.

---


# Pipeline Stages Overview
## Term Count Stage (term_count/)
* Mapper: Tokenizes documents and combines the docid and terms. (docid+term, 1)
* Reducer: Sums term counts for each document. (docid+term, term_count)

## Total Term Count Stage (total_term_count/)
* Mapper: Reads documents and emits data to help compute the total number of terms per document. (docid, 1)
* Reducer: Sums the term counts to produce a total for each document. (docid, term_count)

## Term Frequency (TF) Stage (tf/)
* Mapper: Reads in the term_count output and emits docid, term counts. (docid, term, count)
* Reducer: Sums up the docid term counts and divides by the total terms in each document (docid, term, TF)

## Document Frequency (DF) Stage (df/)
* Mapper: Reads in term_count output and emits each unique term from a document along with the document ID. (term, docid)
* Reducer: Aggregates the term and docid pairs to count in how many documents each term appears. (term, doc_count)

## TF‑IDF Computation Stage (tfidf/):
* Mapper: Reads both TF and DF outputs. Tags each entry to distinguish between TF and DF data. Emits (term, TF|DF, value)
* Reducer: Joins the TF and DF data by term. For each entry, computes TF-IDF score. (docid+term, TF-IDF)


# Running the Pipeline Locally
Below are example commands to simulate each MapReduce job on a Unix-like system. (Adjust paths as needed.)

## Step A: Prepare Your Corpus
Place all your text files (e.g., doc1.txt, doc2.txt, …) in a directory named corpus/.

## Step B: Run the Term Count Job
For each document, run:

```
for file in data/state_union/*.txt; do
    export map_input_file="$file"
    # Run the mapper, sort the output, and pass it to the reducer
    cat "$file" | python3 term_count/mapper.py | sort | python3 term_count/reducer.py
done > output/term_counts.txt
```
This produces a file (term_counts.txt) with term counts per document.

## Step C: Run the Total Term Count Job
Similarly, for each document:

```
for file in data/state_union/*.txt; do
    export map_input_file="$file"
    cat "$file" | python3 total_term_count/mapper.py | sort | python3 total_term_count/reducer.py
done > output/total_term_counts.txt
```
This output gives the total number of terms per document.


## Step D: Run the TF Job
Assuming the TF mapper uses the outputs from the previous steps, you might run:

Example: join term counts and total term counts (the actual command may vary based on your implementation)
```
cat term_counts.txt total_term_counts.txt | python3 tf/mapper.py | sort | python3 tf/reducer.py > tf_results.txt
```
This should produce a file with the term frequency (TF) for each term in each document.

## Step E: Run the DF Job
For each document, run the improved DF mapper and its reducer:

```
for file in corpus/*.txt; do
    export map_input_file="$file"
    cat "$file" | python3 df/mapper.py | sort | python3 df/reducer.py
done > df_results.txt
```
This produces a file with document frequency counts for each term.


## Step F: Compute TF‑IDF
Finally, you’ll need to combine tf_results.txt and df_results.txt (and possibly the total document count) in a final MapReduce job or a join script. This job would typically:

* Join on the term.
* Compute the inverse document frequency (IDF) using a formula such as:
	```
	IDF=log(𝑁 / 𝑑𝑓)
	```
	where N is the total number of documents.
* Multiply the TF and IDF to obtain the TF‑IDF score.
	
If you have a dedicated script for this (say, `tfidf/mapper.py` and a corresponding reducer), run them similarly:

```
cat tf_results.txt df_results.txt | python3 tfidf/mapper.py | sort | python3 tfidf/reducer.py > tfidf_scores.txt
````
**Note: The exact join and computation logic will depend on how you design the final stage. In many implementations, the join is performed via a composite key or by pre-sorting the files before merging.**




---


# How to Run the Pipeline in Hadoop
## Upload your corpus to HDFS (if not done already):
```
hdfs dfs -mkdir -p /input
hdfs dfs -put corpus/* /input/
```

## Run the MapReduce job:
```
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -input /input \
    -output /output \
    -mapper "python3 mapper.py" \
    -reducer "python3 reducer.py" \
    -file term_count/mapper.py \
    -file term_count/reducer.py
```

## Check the results:
```
hdfs dfs -cat /output/part-*
```


