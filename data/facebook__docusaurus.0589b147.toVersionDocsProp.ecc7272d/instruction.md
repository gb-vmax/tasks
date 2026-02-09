# Bug Report

### Describe the bug

I'm experiencing an issue where document lookups in the docs plugin are not working correctly. When trying to access specific documents by their ID, the system appears to be using the wrong key for the lookup, causing documents to be inaccessible or returning incorrect results.

Additionally, all documents seem to be getting assigned the same sidebar configuration instead of their individual sidebar settings.

### Reproduction

```js
// Setup: Create a docs version with multiple documents
const docs = [
  { id: 'intro', title: 'Introduction', sidebar: 'tutorialSidebar' },
  { id: 'guide', title: 'User Guide', sidebar: 'apiSidebar' }
]

// Try to access a document by its ID
const doc = versionDocs['intro']  // This lookup fails

// Also, all documents now share the same sidebar
// Expected: Each doc should have its own sidebar configuration
// Actual: All docs have the sidebar from the first document
```

### Expected behavior

1. Documents should be accessible by their document ID (not title)
2. Each document should retain its own sidebar configuration
3. The document lookup structure should use `doc.id` as the key in the returned object

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems like it might be related to recent changes in how document properties are being mapped. The lookup mechanism appears to have changed unexpectedly.

---
Repository: /testbed
