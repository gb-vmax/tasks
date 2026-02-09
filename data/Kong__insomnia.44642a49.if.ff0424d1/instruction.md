# Bug Report

### Describe the bug

When importing Postman collections, requests with empty raw body strings are not being handled correctly. The body should be preserved as an empty string, but instead it seems to be getting dropped or converted to something else.

### Reproduction

```js
// Postman collection with a request that has an empty raw body
const collection = {
  item: [{
    request: {
      body: {
        mode: 'raw',
        raw: ''  // Empty string body
      }
    }
  }]
}

// After import, the empty body is not preserved correctly
```

### Expected behavior

Requests with empty raw body strings (`raw: ''`) should maintain their body configuration. An empty string is still a valid body value and should be treated differently from a missing/null body.

### System Info
- Insomnia version: latest
- Import format: Postman Collection

---
Repository: /testbed
