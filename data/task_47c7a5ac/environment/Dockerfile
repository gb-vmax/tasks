FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/storage

cat > /home/user/storage/file_audit.log << 'EOF'
204800	alice	/data/projects/report.pdf
512000	bob	/data/projects/summary.pdf
102400	alice	/data/logs/access.log
307200	charlie	/data/media/photo.jpg
819200	alice	/data/projects/presentation.pptx
204800	bob	/data/reports/budget.xlsx
102400	diana	/data/logs/error.log
409600	alice	/data/media/banner.jpg
614400	bob	/data/projects/design.pdf
102400	charlie	/data/scripts/deploy
204800	diana	/data/projects/notes.txt
307200	alice	/data/reports/q1.pdf
204800	bob	/data/logs/server.log
102400	eve	/data/scripts/backup
512000	charlie	/data/projects/data.csv
204800	diana	/data/media/logo.jpg
102400	alice	/data/scripts/setup
307200	bob	/data/media/diagram.jpg
204800	eve	/data/projects/readme.txt
102400	charlie	/data/logs/app.log
409600	alice	/data/data/export.csv
204800	diana	/data/data/import.csv
307200	eve	/data/projects/plan.pdf
102400	bob	/data/scripts/init
204800	charlie	/data/reports/analysis.xlsx
307200	alice	/data/projects/spec.txt
204800	diana	/data/logs/debug.log
512000	eve	/data/data/results.csv
102400	bob	/data/data/config.txt
204800	charlie	/data/media/thumbnail.jpg
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
