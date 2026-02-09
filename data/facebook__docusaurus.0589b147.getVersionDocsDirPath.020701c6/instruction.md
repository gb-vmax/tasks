# Bug Report

### Describe the bug

Versioned docs are not being loaded from the correct directory path. After a recent update, the plugin is looking for versioned documentation in the wrong location, causing version-specific docs to not be found.

### Reproduction

1. Set up a Docusaurus site with versioned docs
2. Create a versioned docs directory following the standard structure: `versioned_docs/version-1.0.0`
3. Try to build or run the site
4. The versioned docs are not loaded/found

### Expected behavior

The plugin should look for versioned docs in the standard `versioned_docs/version-{versionName}` directory structure. For example, if the version is `1.0.0`, it should look in `versioned_docs/version-1.0.0/`.

### Additional context

This seems to affect all versioned documentation. The current behavior appears to be looking in a different directory structure than what's documented and what was working previously.

---
Repository: /testbed
