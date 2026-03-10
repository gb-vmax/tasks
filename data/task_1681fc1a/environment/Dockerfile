FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/data

cat > /home/user/data/sales.csv << 'EOF'
transaction_id,product,quantity,unit_price,region
T001,widget,5,12.50,north
T002,gadget,abc,9.99,south
T003,widget,3,8.00,east
T004,doohickey,2,15.00,west
T005,gadget,1,9.99,
T006,widget,0,12.50,north
T007,thingamajig,4,20.00,south
T008,gadget,2,9.99,midwest
T009,widget,10,12.50,east
T010,doohickey,,15.00,west
T011,gadget,3,9.99,north
T012,thingamajig,1,-5.00,south
T013,doohickey,6,15.00,west
T014,widget,2,8.00
T015,gadget,7,9.99,south
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
