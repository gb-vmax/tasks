Hey, I need help updating two configuration files for our build pipeline before I push the release. We just bumped to version `2.4.1` and I need to make sure both the build config and the artifact manifest are updated consistently.

**File 1: `/home/user/build/build.toml`**

This is our TOML build configuration. I need you to make the following changes:

1. Change the `version` field under the `[package]` section from its current value to `"2.4.1"`.
2. Change the `channel` field under the `[release]` section from its current value to `"stable"`.
3. Add a new field `checksum_required` with the boolean value `true` under the `[release]` section (it doesn't exist yet).

The final `/home/user/build/build.toml` should look exactly like this:

```toml
[package]
name = "myapp"
version = "2.4.1"
authors = ["build-team@example.com"]

[release]
channel = "stable"
checksum_required = true
target = "linux-x86_64"
```

**File 2: `/home/user/build/artifacts.yaml`**

This is our YAML artifact manifest. I need you to make the following changes:

1. Change the `version` field at the top level from its current value to `"2.4.1"`.
2. Change the `environment` field under `metadata` from its current value to `"production"`.
3. Under the `artifacts` list, there is an entry with `name: myapp-binary`. Change its `path` field from its current value to `"dist/myapp-2.4.1-linux-x86_64"`.

The final `/home/user/build/artifacts.yaml` should look exactly like this:

```yaml
version: "2.4.1"
metadata:
  environment: "production"
  owner: "build-team"
artifacts:
  - name: myapp-binary
    path: dist/myapp-2.4.1-linux-x86_64
    type: executable
  - name: myapp-config
    path: dist/myapp-config.tar.gz
    type: archive
```

Please update both files so they match the exact contents shown above. The automated deployment system will validate these files character-by-character, so formatting and field order must match precisely.
