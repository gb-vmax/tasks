# Bug Report

### Describe the bug

When calling `database.all()` to retrieve all documents of a specific type, the function returns incorrect results. Instead of fetching all documents of the requested type, it appears to be passing the string `'all'` as the type parameter to `database.find()`, which causes unexpected behavior.

### Reproduction

```js
// Try to get all documents of a specific type
const requests = await database.all('Request');

// Expected: All Request documents
// Actual: Documents are not returned correctly
```

The issue seems to occur when the database is not empty. The logic for handling the empty vs non-empty database state appears to be inverted.

### Expected behavior

`database.all(type)` should return all documents of the specified type regardless of whether the database is empty or not. The function should properly pass the type parameter through to the underlying query mechanism.

### System Info
- Package: insomnia
- Module: common/database.ts

---
Repository: /testbed
