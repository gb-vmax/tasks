#!/bin/bash
set -e
cd /home/user

cat /home/user/pipeline/process.sh
bash -c '
TIMEFORMAT="%R"
times=()
for i in $(seq 1 10); do
    t=$( { time bash /home/user/pipeline/process.sh; } 2>&1 )
    times+=("$t")
    echo "Run $i: $t"
done

# Compute stats with awk
printf "%s\n" "${times[@]}" | awk "
BEGIN { min=999999; max=0; sum=0; count=0 }
{
    val = \$1 + 0
    if (val < min) min = val
    if (val > max) max = val
    sum += val
    count++
}
END {
    avg = sum / count
    printf \"benchmark: process.sh\nruns: 10\nmin: %.3fs\nmax: %.3fs\navg: %.3fs\n\", min, max, avg
}" | tee /home/user/pipeline/benchmark_report.txt
'
cat /home/user/pipeline/benchmark_report.txt
