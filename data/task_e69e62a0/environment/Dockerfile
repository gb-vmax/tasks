FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/profiling

cat > /home/user/profiling/cpu_profile.tsv << 'EOF'
function_name	module	call_count	avg_latency_us	total_time_us	self_time_us
render_frame	graphics	4200	312	1310400	987600
parse_input	input	18900	45	850500	850500
load_texture	graphics	530	1800	954000	721000
update_physics	engine	4200	275	1155000	634000
audio_mix	audio	8400	98	823200	823200
compress_data	network	210	4200	882000	441000
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
