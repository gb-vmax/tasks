# Bug Report

### Describe the bug

When importing Postman collections with empty string body content, the request body is not being preserved correctly. Instead of maintaining an empty body with the appropriate mime type, the body is being completely removed from the imported request.

### Reproduction

```js
// Postman collection with raw body set to empty string
const postmanCollection = {
  item: [{
    request: {
      body: {
        mode: 'raw',
        raw: '',
        options: {
          raw: {
            language: 'json'
          }
        }
      }
    }
  }]
}

// After import, the body is completely missing instead of being an empty JSON body
```

### Expected behavior

When a Postman request has an empty string as the raw body content, it should still import with the correct mime type preserved. An empty string is a valid body value and should be treated differently from undefined/null body content.

For example, a request with `raw: ''` and `mimeType: 'application/json'` should import as a request with an empty JSON body, not as a request with no body at all.

### System Info
- Insomnia version: latest
- Import source: Postman Collection v2.1

---
Repository: /testbed
