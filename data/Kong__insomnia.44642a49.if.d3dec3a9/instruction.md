# Bug Report

### Describe the bug

The `database.get()` function is not retrieving data correctly. When trying to fetch records by ID, the function returns `undefined` even though the record exists in the database.

### Reproduction

```js
// Create a document
const doc = await database.insert({
  type: 'Request',
  name: 'Test Request',
  // ... other fields
});

// Try to retrieve it
const retrieved = await database.get('Request', doc._id);

// retrieved is undefined, but should be the document
console.log(retrieved); // undefined
```

### Expected behavior

`database.get()` should return the document when a valid type and ID are provided. The function should successfully retrieve existing records from the database.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
