FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e
# Create input data files the agent will work with

mkdir -p /home/user/sales_data

cat > /home/user/sales_data/north.csv <<EOF
OrderID,Product,Region,Salesperson,Quantity,SaleAmount
1001,WidgetA,North,Alice,3,250.00
1002,WidgetB,North,Bob,2,180.50
1003,WidgetA,North,Charlie,5,425.00
EOF

cat > /home/user/sales_data/south.csv <<EOF
OrderID,Product,Region,Salesperson,Quantity,SaleAmount
2001,WidgetC,South,David,1,90.00
2002,WidgetA,South,Emily,4,340.00
EOF

cat > /home/user/sales_data/west.csv <<EOF
OrderID,Product,Region,Salesperson,Quantity,SaleAmount
3001,WidgetB,West,Frank,2,200.00
3002,WidgetD,West,Gina,3,315.00
3003,WidgetC,West,Hank,1,110.00
3004,WidgetA,West,Irene,2,170.00
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
