I'm an observability engineer managing Grafana dashboard configurations across multiple environments. We keep versioned dashboard JSON templates and use symlinks to "activate" specific versions per environment, so we can roll back quickly without copying files.

Our current setup at `/home/user/dashboards` is a bit of a mess after some recent migrations. I need you to audit and reorganize everything according to the rules below. Here's the full directory layout that currently exists:

```
/home/user/dashboards/
  templates/
    infra/
      nodes_v1.json
      nodes_v2.json
      nodes_v3.json
    app/
      latency_v1.json
      latency_v2.json
      requests_v1.json
      requests_v2.json
      requests_v3.json
    db/
      queries_v1.json
      queries_v2.json
  active/
    production/
      nodes.json        -> ../../templates/infra/nodes_v1.json   (symlink, currently outdated)
      latency.json      -> ../../templates/app/latency_v2.json   (symlink, correct)
      requests.json     -> ../../templates/app/requests_v2.json  (symlink, outdated)
    staging/
      nodes.json        -> ../../templates/infra/nodes_v2.json   (symlink)
      latency.json      -> ../../templates/app/latency_v1.json   (symlink, outdated)
      requests.json     -> ../../templates/app/requests_v3.json  (symlink, correct)
    development/
      (currently empty — no symlinks set up yet)
  archive/
    (currently empty)
```

Please do all of the following:

**Step 1: Upgrade production symlinks**
The production environment must always point to the latest version of every template. Update these symlinks:
- `active/production/nodes.json` → should point to `../../templates/infra/nodes_v3.json`
- `active/production/requests.json` → should point to `../../templates/app/requests_v3.json`
- `active/production/latency.json` is already correct — leave it alone.
Also add a new symlink `active/production/queries.json` → `../../templates/db/queries_v2.json`

**Step 2: Fix the staging symlink**
Update `active/staging/latency.json` → should point to `../../templates/app/latency_v2.json` (currently pointing to v1).

**Step 3: Set up development environment**
Development should mirror staging exactly. Create symlinks in `active/development/`:
- `nodes.json` → `../../templates/infra/nodes_v2.json`
- `latency.json` → `../../templates/app/latency_v2.json`
- `requests.json` → `../../templates/app/requests_v3.json`
- `queries.json` → `../../templates/db/queries_v1.json`

**Step 4: Archive an old template**
Move `templates/infra/nodes_v1.json` into the `archive/` directory. Then create a symlink at `archive/nodes_v1.json` that points back to itself using a relative path: `../archive/nodes_v1.json` is the file itself, so the symlink should be placed at `templates/infra/nodes_v1.json` and point to `../../archive/nodes_v1.json` — this way any system still referencing that path will resolve to the archived copy.

**Step 5: Generate an audit report**
Write a file `/home/user/dashboards/audit_report.txt` with the following exact format. Each symlink in the `active/` subdirectories should be listed. Sort the entries: first by environment name alphabetically (development, production, staging), then within each environment by symlink name alphabetically. Use `readlink` semantics — show the literal target string stored in the symlink (i.e., the relative path as created, not the resolved absolute path).

The format must be exactly:
```
=== Dashboard Symlink Audit ===

[development]
  latency.json -> ../../templates/app/latency_v2.json
  nodes.json -> ../../templates/infra/nodes_v2.json
  queries.json -> ../../templates/db/queries_v1.json
  requests.json -> ../../templates/app/requests_v3.json

[production]
  latency.json -> ../../templates/app/latency_v2.json
  nodes.json -> ../../templates/infra/nodes_v3.json
  queries.json -> ../../templates/db/queries_v2.json
  requests.json -> ../../templates/app/requests_v3.json

[staging]
  latency.json -> ../../templates/app/latency_v2.json
  nodes.json -> ../../templates/infra/nodes_v2.json
  queries.json -> ../../templates/db/queries_v1.json (MISSING TARGET)
  requests.json -> ../../templates/app/requests_v3.json

Total symlinks: 12
```

Wait — note that `active/staging/queries.json` does NOT exist (we never created it). So the staging section should only have 3 entries. The correct final report format is:

```
=== Dashboard Symlink Audit ===

[development]
  latency.json -> ../../templates/app/latency_v2.json
  nodes.json -> ../../templates/infra/nodes_v2.json
  queries.json -> ../../templates/db/queries_v1.json
  requests.json -> ../../templates/app/requests_v3.json

[production]
  latency.json -> ../../templates/app/latency_v2.json
  nodes.json -> ../../templates/infra/nodes_v3.json
  queries.json -> ../../templates/db/queries_v2.json
  requests.json -> ../../templates/app/requests_v3.json

[staging]
  latency.json -> ../../templates/app/latency_v2.json
  nodes.json -> ../../templates/infra/nodes_v2.json
  requests.json -> ../../templates/app/requests_v3.json

Total symlinks: 11
```

Each line in the per-environment sections starts with exactly two spaces, then the symlink filename, then ` -> `, then the literal symlink target. There is a blank line between each environment block and before `Total symlinks:`. The total count is the sum of all symlinks across all three environment directories.

Also verify that `templates/infra/nodes_v1.json` no longer exists as a regular file in that location (it was moved to `archive/`) but DOES exist as a symlink pointing to `../../archive/nodes_v1.json`, and that `archive/nodes_v1.json` is a regular file.
