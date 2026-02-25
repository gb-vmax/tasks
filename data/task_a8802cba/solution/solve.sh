#!/bin/bash
set -e
cd /home/user

sed -i '/name: APP_ENVIRONMENT/{n;s/value: development/value: production/;}' /home/user/deploy_settings.yaml
sed -i '/name = "APP_ENVIRONMENT"/{n;s/value = "development"/value = "production"/;}' /home/user/deploy_settings.toml
echo "YAML APP_ENVIRONMENT: $(awk '/name: APP_ENVIRONMENT/{getline; print $2}' /home/user/deploy_settings.yaml)
TOML APP_ENVIRONMENT: $(awk '$0 ~ /name = "APP_ENVIRONMENT"/{getline; match($0, /value = "(.*)"/, arr); print arr[1]}' /home/user/deploy_settings.toml)" > /home/user/config_update.log
YAML_VAL=$(awk '/name: APP_ENVIRONMENT/{getline; print $2}' /home/user/deploy_settings.yaml); TOML_VAL=$(awk '/name = "APP_ENVIRONMENT"/{getline; if($0 ~ /value =/){gsub(/"/,""); print $3}}' /home/user/deploy_settings.toml); echo -e "YAML APP_ENVIRONMENT: $YAML_VAL\nTOML APP_ENVIRONMENT: $TOML_VAL" > /home/user/config_update.log
cat /home/user/config_update.log
