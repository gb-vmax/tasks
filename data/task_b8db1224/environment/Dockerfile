FROM endless-base:latest
RUN <<'ENDSETUP'
#!/bin/bash
set -e

mkdir -p /home/user/mlops

cat > /home/user/mlops/experiments.tsv << 'EOF'
exp_001	resnet50	COMPLETED	0.9234	/mnt/storage/runs/exp_001/ckpt_final.pt
exp_002	bert_base	FAILED	0.0000	/mnt/storage/runs/exp_002/ckpt_epoch3.pt
exp_003	vgg16	COMPLETED	0.8751	/mnt/storage/runs/exp_003/ckpt_best.pt
exp_004	efficientnet	RUNNING	0.6100	/mnt/storage/runs/exp_004/ckpt_epoch10.pt
exp_005	bert_large	COMPLETED	0.9512	/mnt/storage/runs/exp_005/ckpt_final.pt
exp_006	resnet101	FAILED	0.0000	/mnt/storage/runs/exp_006/ckpt_epoch1.pt
exp_007	mobilenet	COMPLETED	0.8103	/mnt/storage/runs/exp_007/ckpt_best.pt
EOF

chown -R user:user /home/user
ENDSETUP

WORKDIR /home/user
