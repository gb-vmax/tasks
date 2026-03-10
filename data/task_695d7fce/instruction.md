I'm a technical writer and I need help updating two configuration files for our documentation site. I've just promoted a new release and need to update the metadata in both our YAML front-matter config and our TOML site config to reflect the new version and publication status.

There are two files:

**File 1:** `/home/user/docs/site_config.toml`

This TOML file has a `[release]` section. I need you to:
- Change the `version` field to `"2.4.0"`
- Change the `status` field to `"stable"`
- Change the `draft` field to `false`

**File 2:** `/home/user/docs/metadata.yaml`

This YAML file has a top-level structure with a `publication` key. I need you to:
- Change `publication.version` to `"2.4.0"`
- Change `publication.stage` to `"stable"`
- Change `publication.last_updated` to `"2024-06-01"`

After your edits, the files must be valid in their respective formats. Please make the edits in place — do not move or rename the files.

The final `/home/user/docs/site_config.toml` `[release]` section must look exactly like:

```toml
[release]
version = "2.4.0"
status = "stable"
draft = false
```

The final `/home/user/docs/metadata.yaml` `publication` block must look exactly like:

```yaml
publication:
  version: "2.4.0"
  stage: "stable"
  last_updated: "2024-06-01"
```

All other fields and sections in both files must remain unchanged.
