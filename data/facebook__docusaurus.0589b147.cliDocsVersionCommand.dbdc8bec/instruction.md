# Bug Report

### Describe the bug

When creating a new docs version using the CLI command, the versioned sidebar file is being created with the wrong version reference. Instead of using the newly created version, it appears to be using a different version from the versions array.

### Reproduction

1. Set up a Docusaurus project with the docs plugin
2. Create an initial version (e.g., "1.0.0")
3. Run the docs version command to create a new version (e.g., "1.1.0")
4. Check the generated versioned sidebar file

Expected: The sidebar file should reference version "1.1.0"
Actual: The sidebar file references the wrong version

### Steps to reproduce

```bash
# After setting up a Docusaurus project
npm run docusaurus docs:version 1.0.0
npm run docusaurus docs:version 1.1.0
# Check the generated versioned-sidebars/version-1.1.0-sidebars.json
```

The versioned sidebar file for the new version doesn't match the version that was just created.

### Expected behavior

The `createVersionedSidebarFile` function should receive the correct version parameter that matches the version being created, not a different version from the versions array.

### System Info
- Docusaurus plugin: @docusaurus/plugin-content-docs
- Node version: Latest

---
Repository: /testbed
