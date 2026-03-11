FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

# Create credentials directory
mkdir -p /home/user/credentials

# Create db_creds.tsv (tab-separated)
printf 'password\tusername\thost\tport\tservice\n' > /home/user/credentials/db_creds.tsv
printf 's3cr3tDB1\talice\tdb1.internal\t5432\tpostgres\n' >> /home/user/credentials/db_creds.tsv
printf 'hunter2\tbob\tdb2.internal\t5432\tpostgres\n' >> /home/user/credentials/db_creds.tsv
printf 'p@ssw0rd\tcarol\tdb3.internal\t3306\tmysql\n' >> /home/user/credentials/db_creds.tsv

# Create api_creds.tsv (tab-separated)
printf 'service\thost\tusername\tapi_key\texpiry\n' > /home/user/credentials/api_creds.tsv
printf 'payments\tapi.payments.io\tsvc_pay\ttok_abc123\t2024-12-31\n' >> /home/user/credentials/api_creds.tsv
printf 'analytics\tapi.analytics.io\tsvc_ana\ttok_xyz789\t2024-11-30\n' >> /home/user/credentials/api_creds.tsv
printf 'notifications\tapi.notify.io\tsvc_not\ttok_def456\t2025-01-15\n' >> /home/user/credentials/api_creds.tsv

# Create ssh_creds.tsv (tab-separated)
printf 'host\tusername\tkey_fingerprint\tport\tservice\n' > /home/user/credentials/ssh_creds.tsv
printf 'jump1.internal\tdeploy\tSHA256:aabbcc1\t22\tbastion\n' >> /home/user/credentials/ssh_creds.tsv
printf 'jump2.internal\tdeploy\tSHA256:ddeeff2\t2222\tbastion\n' >> /home/user/credentials/ssh_creds.tsv
printf 'worker1.internal\tansible\tSHA256:112233a\t22\tautomation\n' >> /home/user/credentials/ssh_creds.tsv

# Set ownership
chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
