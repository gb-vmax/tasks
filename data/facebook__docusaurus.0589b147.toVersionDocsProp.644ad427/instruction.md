# Bug Report

### Describe the bug

After a recent update, the docs plugin is behaving strangely. When trying to access document metadata in my site, the document IDs and structure seem completely wrong. The document lookup appears to be broken - instead of using the actual document ID, it seems like the title is being used as the key, and the ID field itself contains the description instead of the actual ID.

### Reproduction

```js
// In a custom component or plugin
const versionDocs = useVersionDocs();

// Try to access a document by its ID
const myDoc = versionDocs['my-document-id'];

// Expected: myDoc.id === 'my-document-id'
// Actual: Document not found, or if accessed by title, myDoc.id contains the description
```

Steps to reproduce:
1. Create a docs site with the docs plugin
2. Try to reference a document by its ID programmatically
3. The document lookup fails or returns incorrect data

### Expected behavior

Documents should be keyed by their actual `id` field, and the `id` property of each document should contain the document's ID, not its description.

### System Info

- Docusaurus version: latest
- Node version: 18.x

This is breaking our custom navigation components that rely on looking up documents by ID. Any help would be appreciated!

---
Repository: /testbed
