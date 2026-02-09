# Bug Report

### Describe the bug

I'm experiencing an issue with the documentation versioning system where the current version appears at the end of the version list instead of at the beginning. This causes the version selector dropdown to show versions in the wrong order, with the current/latest version appearing last rather than first.

### Reproduction

```js
// Setup a docs plugin with versioning enabled
const docsPluginOptions = {
  id: 'default',
  includeCurrentVersion: true,
  // ... other options
}

// When versions are loaded, the current version is appended 
// to the end instead of being prepended to the start
```

Steps to reproduce:
1. Configure a Docusaurus site with docs versioning
2. Set `includeCurrentVersion: true` in the docs plugin options
3. Create a few versioned docs (e.g., version-1.0, version-2.0)
4. Check the order of versions in the version selector

### Expected behavior

The current version should appear first in the version list (at the beginning), not last. The typical expected order would be:
- Current (latest)
- 2.0
- 1.0

But instead I'm seeing:
- 2.0
- 1.0  
- Current (latest)

This affects the user experience as visitors expect to see the latest/current version at the top of the dropdown.

### Additional context

This seems to have changed recently and is affecting the version ordering logic. The current version should be prioritized and shown first in the list.

---
Repository: /testbed
