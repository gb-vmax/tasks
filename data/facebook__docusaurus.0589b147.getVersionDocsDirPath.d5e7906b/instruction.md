# Bug Report

### Describe the bug

When trying to access versioned docs, the plugin is looking for the wrong directory structure. The versioned docs directory path is being constructed incorrectly, causing docs to not be found.

### Reproduction

1. Set up a Docusaurus project with versioned documentation
2. Create a versioned docs folder following the standard structure: `versioned_docs/version-1.0.0`
3. Try to build or serve the site
4. The versioned docs are not loaded correctly

### Expected behavior

The plugin should correctly locate versioned docs in the `versioned_docs/version-{versionName}` directory structure (e.g., `versioned_docs/version-1.0.0`).

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
