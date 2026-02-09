# Bug Report

### Describe the bug

When creating a new docs version using the CLI command, the version check logic is inverted. The command throws an error saying "this version already exists" when trying to create a version that doesn't exist yet, and allows creating duplicate versions when a version already exists.

### Reproduction

```bash
# First time creating version 1.0.0 - this should work but throws error
npx docusaurus docs:version 1.0.0
# Error: [docs]: this version already exists! Use a version tag that does not already exist.

# If you somehow bypass this and run it again with same version
# It should throw error but doesn't - creates duplicate
```

### Expected behavior

The command should:
1. Allow creating a new version when it doesn't exist in versions.json
2. Throw an error when trying to create a version that already exists

Currently it's doing the opposite - blocking new versions and allowing duplicates.

### Additional context

Also noticed that new versions are being added to the end of the versions array instead of the beginning, which might affect version ordering.

---
Repository: /testbed
