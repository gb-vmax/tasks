# Bug Report

### Describe the bug

I'm encountering an issue where document lookups in the version docs prop are failing. When trying to access documents by their ID, I'm getting undefined values even though the documents exist in the version.

### Reproduction

```js
const versionDocs = toVersionDocsProp(loadedVersion);

// Trying to access a document by its ID
const doc = versionDocs['my-doc-id'];
console.log(doc); // Returns undefined

// But the document exists in loadedVersion.docs with id 'my-doc-id'
```

### Expected behavior

Documents should be accessible by their ID in the returned object. The `toVersionDocsProp` function should create a mapping where document IDs are the keys, allowing direct access like `versionDocs[docId]`.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have broken document navigation and sidebar generation in my project. Any help would be appreciated!

---
Repository: /testbed
