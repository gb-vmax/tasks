# Bug Report

### Describe the bug

The `docs:version` CLI command is not working as expected. When I try to create a new documentation version, it's behaving strangely in two ways:

1. The new version appears at the end of the versions list instead of at the beginning
2. The command fails when the docs folder actually contains files (which should be the normal case)

### Reproduction

```bash
# Set up a docs folder with some markdown files
mkdir -p docs
echo "# Test" > docs/intro.md

# Try to create a new version
npm run docusaurus docs:version 1.0.0
```

This throws an error saying the docs directory is empty or doesn't exist, even though it clearly has files in it.

Also, if you manage to get past that error (by having an empty docs folder somehow), the version gets added to the end of the `versions.json` array instead of the beginning. So instead of:

```json
["1.0.0", "0.9.0"]
```

You get:

```json
["0.9.0", "1.0.0"]
```

This breaks the expected version ordering where newer versions should appear first.

### Expected behavior

- The command should work when the docs folder contains markdown files (not when it's empty)
- New versions should be added to the beginning of the versions array, not the end

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
