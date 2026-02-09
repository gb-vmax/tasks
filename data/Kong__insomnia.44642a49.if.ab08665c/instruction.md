# Bug Report

### Describe the bug
The database `get` function is not returning any data when the database is populated. It seems like the logic for checking if the database is empty got inverted somehow, causing it to only work when the database is actually empty.

### Reproduction
```js
// Assume database has been initialized and contains data
const result = await database.get('Request', 'req_123');
console.log(result); // Returns undefined instead of the request object

// The function only seems to work when the database is empty
// which is the opposite of what should happen
```

### Expected behavior
The `get` function should return the requested object when the database contains data. It should only return early (undefined) when the database is empty.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
