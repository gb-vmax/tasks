#!/bin/bash
set -e
cd /home/user

cat /home/user/cloud/services.csv
head -1 /home/user/cloud/services.csv > /home/user/cloud/to_migrate.csv && awk -F',' 'NR>1 && $2=="us-east-1" && $3=="production"' /home/user/cloud/services.csv >> /home/user/cloud/to_migrate.csv
cat /home/user/cloud/to_migrate.csv
awk -F',' '
BEGIN {
    print "MIGRATION MANIFEST: us-east-1 -> eu-west-2"
    print "----------------------------------------"
    count = 0
    total = 0
}
NR > 1 {
    print "[SERVICE] " $1 " | replicas=" $5 " | est_cost=$" $4
    count++
    total += $4
}
END {
    print "----------------------------------------"
    print "Total services: " count
    print "Total monthly cost: $" total
}
' /home/user/cloud/to_migrate.csv > /home/user/cloud/migration_manifest.txt
cat /home/user/cloud/migration_manifest.txt
chmod 644 /home/user/cloud/migration_manifest.txt
ls -l /home/user/cloud/migration_manifest.txt /home/user/cloud/to_migrate.csv
