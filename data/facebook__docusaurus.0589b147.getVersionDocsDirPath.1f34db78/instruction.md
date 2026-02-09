# Bug Report

### Describe the bug

The versioned docs directory path is being generated incorrectly. After a recent change, the version name is being placed before the `versioned_docs` directory instead of after it, and the `version-` prefix is missing.

### Reproduction

When trying to access versioned documentation, the path resolution fails because it's looking in the wrong directory structure.

Expected directory structure:
```
siteDir/
  versioned_docs/
    version-1.0.0/
```

But the code is now generating:
```
siteDir/
  1.0.0/
    versioned_docs/
```

This breaks versioned documentation loading as the files can't be found in the expected location.

### Steps to reproduce:
1. Set up a Docusaurus site with versioned docs
2. Create a version (e.g., version 1.0.0)
3. Try to build or serve the site
4. Versioned docs won't load correctly due to incorrect path resolution

### Expected behavior

The `getVersionDocsDirPath` function should generate paths in the format:
`siteDir/versioned_docs/version-{versionName}`

With the version prefix included and the proper directory ordering.

### System Info
- Docusaurus plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
