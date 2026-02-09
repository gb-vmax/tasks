# Bug Report

### Describe the bug

When importing Postman collections with requests that have no query parameters, the import process fails or produces unexpected results. It seems like the parameter handling has regressed and now returns `null` instead of an empty array when there are no parameters to import.

### Reproduction

```js
// Import a Postman collection with a request that has no query parameters
const postmanCollection = {
  item: [{
    request: {
      url: {
        query: [] // Empty query parameters
      }
    }
  }]
}

// Try to import this collection
// Expected: Should import successfully with empty parameters array
// Actual: Import fails or produces null parameters
```

### Expected behavior

When a request has no query parameters (empty array), the importer should return an empty array `[]` for the parameters field. This maintains consistency with the rest of the codebase which expects parameters to be an array type.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
