# Bug Report

### Describe the bug

I'm experiencing an issue where document references in the docs plugin are not working correctly. When trying to access a document by its ID, I'm getting undefined or the wrong document. It seems like the document lookup mechanism has broken.

### Reproduction

```js
// In a component or plugin
const versionDocs = getVersionDocs();

// Try to access a document by its ID
const myDoc = versionDocs['my-doc-id'];
// Returns undefined even though the document exists

// Also, documents with the same title overwrite each other
// If you have two docs with title "Introduction", only one is accessible
```

### Steps to reproduce:
1. Create a docs version with multiple documents
2. Try to reference a document using its ID (e.g., in sidebar config or custom component)
3. The document is not found or returns undefined
4. If multiple documents share the same title, they collide and overwrite each other in the lookup

### Expected behavior

Documents should be accessible by their unique ID, not by their title. Using titles as keys can cause:
- Documents with the same title to overwrite each other
- Breaking existing code that references documents by ID
- Inability to reliably look up specific documents

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is breaking my documentation site where I need to programmatically access documents by their IDs. Any help would be appreciated!

---
Repository: /testbed
