# Bug Report

### Describe the bug

After a recent update, versioned sidebars are not being loaded correctly. The documentation site fails to find the sidebar configuration files for versioned docs, resulting in broken navigation for older versions.

### Reproduction

1. Set up a Docusaurus site with versioned documentation
2. Create a new version using the versioning command
3. Try to build or serve the site
4. The sidebar configuration for versioned docs cannot be found

The issue appears to be related to how the sidebar file paths are being constructed. The system is looking for files in the wrong location or with an incorrect naming pattern.

### Expected behavior

Versioned sidebars should be loaded from the correct path with the proper filename format. The navigation should work correctly for all versioned documentation.

### System Info

- Docusaurus version: Latest
- Node version: 18.x
- Plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
