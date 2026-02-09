# Bug Report

### Describe the bug

When importing Postman collections with raw request bodies, empty string bodies are not being handled correctly. The importer returns an empty object `{}` instead of properly structured body data with `mimeType` and `text` fields.

### Reproduction

```js
// Import a Postman request with an empty raw body
const request = {
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

// The imported body returns {} instead of the expected format
// Expected: { mimeType: 'application/json', text: '' }
// Actual: {}
```

### Expected behavior

Even when the raw body is an empty string, the importer should return a consistent structure with `mimeType` and `text` properties. This ensures that the imported request maintains the correct content type information and doesn't break downstream processing that expects these fields to be present.

### Additional context

This affects requests that have a content type specified but no actual body content. The empty object return breaks the expected data structure and can cause issues when the imported data is used elsewhere in the application.

---
Repository: /testbed
