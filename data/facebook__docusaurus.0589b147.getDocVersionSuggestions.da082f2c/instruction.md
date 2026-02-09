# Bug Report

### Describe the bug

The `getDocVersionSuggestions` function is returning incorrect values for `latestDocSuggestion` and `latestVersionSuggestion`. It looks like the returned object has the wrong assignments - the latest doc suggestion is being set to a version object instead of a doc, and the latest version suggestion is being set to a doc instead of a version.

### Reproduction

```js
const data = {
  versions: [
    { name: 'current', docs: [...] },
    { name: '1.0.0', docs: [...] }
  ],
  alternateDocVersions: {
    'current': { id: 'intro', path: '/docs/intro' }
  }
};

const result = getDocVersionSuggestions(data, '/docs/1.0.0/intro');

// Expected:
// result.latestDocSuggestion = { id: 'intro', path: '/docs/intro' }
// result.latestVersionSuggestion = { name: 'current', docs: [...] }

// Actual:
// result.latestDocSuggestion = { name: 'current', docs: [...] }  // Wrong! This is a version
// result.latestVersionSuggestion = { id: 'intro', path: '/docs/intro' }  // Wrong! This is a doc
```

### Expected behavior

The function should return:
- `latestDocSuggestion`: The doc object from the latest version
- `latestVersionSuggestion`: The latest version object

Currently these values appear to be swapped, causing issues when trying to use them for version suggestions in the docs plugin.

---
Repository: /testbed
