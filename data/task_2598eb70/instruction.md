Hey, I need help updating two microservice configuration files before deploying to production. I've got a YAML file for our API gateway and a TOML file for our message broker service, and I need specific values changed in both.

The files are at:
- `/home/user/services/gateway/config.yaml`
- `/home/user/services/broker/config.toml`

**Changes needed for `config.yaml`:**

The API gateway is getting a replica count bump and a memory limit increase for the production push. Please make the following changes:
1. Change `replicas` from its current value to `4`
2. Change the `memory` limit under `resources.limits` from its current value to `1024Mi`
3. Change the `image.tag` from its current value to `v2.5.1`

**Changes needed for `config.toml`:**

The message broker needs its connection pool and timeout settings updated:
1. Change `max_connections` under `[pool]` from its current value to `200`
2. Change `timeout_seconds` under `[pool]` from its current value to `30`
3. Change `enabled` under `[telemetry]` from its current value to `true`

The files must remain valid YAML and TOML respectively after editing — don't mangle the surrounding structure. All other fields should stay exactly as they are.

After you've made the edits, can you verify both files look correct by printing them out?
