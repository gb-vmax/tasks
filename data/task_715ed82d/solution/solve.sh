#!/bin/bash
set -e
cd /home/user

cat /home/user/mlops/artifact_registry/VERSION
cat /home/user/mlops/artifact_registry/CHANGELOG.md
echo "1.4.8" > /home/user/mlops/artifact_registry/VERSION
printf '## [1.4.8] - 2024-11-15\n\n### Fixed\n- Preprocessing pipeline: reject NaN values during feature normalization step\n\n' | cat - /home/user/mlops/artifact_registry/CHANGELOG.md > /tmp/CHANGELOG_new.md && mv /tmp/CHANGELOG_new.md /home/user/mlops/artifact_registry/CHANGELOG.md
cat /home/user/mlops/artifact_registry/VERSION && echo "---" && cat /home/user/mlops/artifact_registry/CHANGELOG.md
