#!/bin/bash
set -e
cd /home/user

ajv validate -s /home/user/artifacts.schema.json -d /home/user/artifacts.json --strict=false
python3 -m jsonschema -i /home/user/artifacts.json /home/user/artifacts.schema.json
jq '[.[] | select(.type == "checkpoint") | {artifact_id, created_at}] | sort_by(.created_at)' /home/user/artifacts.json > /home/user/checkpoint_summary.json
cat /home/user/checkpoint_summary.json
