FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/support

cat > /home/user/support/tickets.tsv << 'EOF'
ticket_id	date	category	technician	status	error_code	priority
T001	2024-01-02	network	alice	closed	ERR_TIMEOUT	high
T002	2024-01-02	hardware	bob	closed	ERR_DISK	medium
T003	2024-01-03	software	carol	open	ERR_CRASH	low
T004	2024-01-03	network	alice	closed	ERR_TIMEOUT	high
T005	2024-01-04	software	dave	closed	ERR_CRASH	medium
T006	2024-01-04	hardware	bob	pending	ERR_DISK	low
T007	2024-01-05	network	carol	closed	ERR_TIMEOUT	high
T008	2024-01-05	access	alice	closed	ERR_AUTH	medium
T009	2024-01-06	software	dave	open	ERR_CRASH	low
T010	2024-01-06	email	bob	closed	ERR_SMTP	medium
T011	2024-01-07	network	alice	closed	ERR_TIMEOUT	high
T012	2024-01-07	hardware	carol	closed	ERR_DISK	medium
T013	2024-01-08	software	dave	pending	ERR_CRASH	low
T014	2024-01-08	access	alice	closed	ERR_AUTH	high
T015	2024-01-09	email	bob	open	ERR_SMTP	medium
T016	2024-01-09	network	carol	closed	ERR_TIMEOUT	high
T017	2024-01-10	software	alice	closed	ERR_CRASH	medium
T018	2024-01-10	hardware	dave	closed	ERR_DISK	low
T019	2024-01-11	access	bob	closed	ERR_AUTH	medium
T020	2024-01-11	email	carol	closed	ERR_SMTP	low
T021	2024-01-12	network	dave	open	ERR_TIMEOUT	high
T022	2024-01-12	software	alice	closed	ERR_CRASH	medium
T023	2024-01-13	hardware	bob	closed	ERR_DISK	low
T024	2024-01-13	access	carol	pending	ERR_AUTH	medium
T025	2024-01-14	email	dave	closed	ERR_SMTP	high
T026	2024-01-14	network	alice	closed	ERR_TIMEOUT	high
T027	2024-01-15	software	bob	open	ERR_CRASH	low
T028	2024-01-15	hardware	carol	closed	ERR_DISK	medium
T029	2024-01-16	access	dave	closed	ERR_AUTH	low
T030	2024-01-16	email	alice	closed	ERR_SMTP	medium
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
