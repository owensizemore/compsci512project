Problems used:
p00018
p00003
p00005
p00019
p03252
p03285

Hadoop job:
hadoop jar /usr/lib/hadoop/hadoop-streaming-3.3.6.jar \
    -files
    gs://p00018/jobs/mapper.py,gs://p00018/jobs/reducer.py
    -mapper
    python3 mapper.py
    -reducer
    python3 reducer.py
    -input
    gs://p00018/input/
    -output
    gs://p00018/output-run1/