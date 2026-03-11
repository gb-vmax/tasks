FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/cost_reports/subdir

python3 -c "open('/home/user/cost_reports/daily_2024_01_15.csv','w').write('A'*15000)"
python3 -c "open('/home/user/cost_reports/daily_2024_01_16.csv','w').write('A'*22000)"
python3 -c "open('/home/user/cost_reports/subdir/daily_2024_01_17.csv','w').write('A'*18500)"
python3 -c "open('/home/user/cost_reports/daily_2024_01_14.csv','w').write('B'*8000)"
python3 -c "open('/home/user/cost_reports/monthly_2024_01.csv','w').write('C'*25000)"
python3 -c "open('/home/user/cost_reports/subdir/monthly_2024_02.csv','w').write('C'*12000)"

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
