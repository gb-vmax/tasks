#!/bin/bash
set -e
cd /home/user

echo '#!/bin/bash
sum=$(awk -F, "NR>1 {s+=\$3} END {print s}" /home/user/data/sales_data.csv)
echo "Total Sales Amount: $sum" | tee /home/user/data/sales_summary.txt
' > /home/user/data/summarize_sales.sh && chmod +x /home/user/data/summarize_sales.sh
/home/user/data/summarize_sales.sh
cat /home/user/data/sales_summary.txt
