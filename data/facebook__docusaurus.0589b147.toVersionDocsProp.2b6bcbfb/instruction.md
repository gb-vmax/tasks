# Bug Report

### Describe the bug

I'm experiencing an issue where document lookup in versioned docs is not working correctly. When trying to access documents by their ID, I'm getting `undefined` instead of the expected document data.

### Reproduction

```js
// Assuming we have a document with id: 'getting-started' and title: 'Getting Started Guide'
const versionDocs = toVersionDocsProp(loadedVersion);

// This now returns undefined
const doc = versionDocs['getting-started'];

// But this works (which is unexpected)
const doc = versionDocs['Getting Started Guide'];
```

The documents seem to be keyed by title instead of ID now, which breaks existing code that relies on looking up documents by their ID.

### Expected behavior

Documents should be accessible using their document ID as the key, not the title. The ID is the stable identifier and should be used for lookups.

### Additional context

This is causing issues in my plugin that needs to reference specific documents by their IDs. Also noticed that the `description` field seems to be missing from the document props now, which I was also using.

---
Repository: /testbed
