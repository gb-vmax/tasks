# Bug Report

### Describe the bug

When navigating to a documentation page, only the first matching document is being returned instead of collecting all alternate versions across different versions. The `getAlternateVersionDocs` function seems to stop after finding the first matching document ID and doesn't continue searching through remaining versions.

### Reproduction

```js
// Given a docs structure with multiple versions:
const data = {
  versions: [
    {
      name: 'current',
      docs: [{ id: 'intro', path: '/docs/intro' }]
    },
    {
      name: '2.0.0',
      docs: [{ id: 'intro', path: '/docs/2.0.0/intro' }]
    },
    {
      name: '1.0.0',
      docs: [{ id: 'intro', path: '/docs/1.0.0/intro' }]
    }
  ]
};

// Call getActiveDocContext with a pathname
const context = getActiveDocContext(data, '/docs/intro');

// Expected: alternateDocVersions should contain entries for all versions
// Actual: alternateDocVersions only contains the first version found
```

### Expected behavior

The `alternateDocVersions` object should contain all versions of a document with the same ID across different documentation versions. For example, if a document with ID 'intro' exists in versions 'current', '2.0.0', and '1.0.0', all three should be included in the result.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is affecting the version switcher functionality - users can't see or switch to alternate versions of the same document.

---
Repository: /testbed
