Hey, I need help updating the configuration files for our documentation site. I'm a technical writer and we just released version 2.1.0 of our software, so I need to update two config files before I can publish the new docs.

There are two config files:
- `/home/user/docs/mkdocs.yml` — the MkDocs configuration file
- `/home/user/docs/site.toml` — the site metadata TOML file

**Changes needed in `/home/user/docs/mkdocs.yml`:**

1. Change the `site_name` field from its current value to `"Procyon Docs v2.1.0"`
2. Change the `site_description` field to `"Official documentation for Procyon 2.1.0"`
3. Under the `extra` section, change the `version` field to `"2.1.0"`
4. Under the `extra` section, change the `release_stage` field to `"stable"`

**Changes needed in `/home/user/docs/site.toml`:**

1. In the `[metadata]` table, change the `version` field to `"2.1.0"`
2. In the `[metadata]` table, change the `last_updated` field to `"2024-11-15"`
3. In the `[metadata]` table, change the `status` field to `"stable"`
4. In the `[build]` table, change the `output_dir` field to `"dist/2.1.0"`

Please make only those specific changes — don't alter any other fields, comments, or formatting in either file. The files should remain valid YAML and TOML respectively after your edits.
