# Bug Report

### Describe the bug

When importing Postman collections with raw body content, empty string bodies are not being handled correctly. The importer returns an empty object `{}` instead of properly structured body data with mimeType and text fields.

### Reproduction

```js
// Importing a Postman request with empty raw body
const postmanRequest = {
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

// Current behavior: returns {}
// Expected: should return { mimeType: 'application/json', text: '' }
```

### Steps to reproduce:
1. Create a Postman collection with a request that has an empty raw body
2. Set the body mode to 'raw' with a specific content type (e.g., JSON)
3. Import the collection into Insomnia
4. The body configuration is lost/incomplete

### Expected behavior

Even when the raw body content is an empty string, the importer should still return a properly structured body object with the appropriate `mimeType` and `text` fields. This ensures that the content type information is preserved during import.

The expected output should be:
```js
{
  mimeType: 'application/json', // or whatever the specified type is
  text: ''
}
```

### System Info
- Insomnia version: latest
- Import source: Postman Collection v2.1

This is causing issues when trying to preserve request configurations during migration from Postman to Insomnia.

---
Repository: /testbed
