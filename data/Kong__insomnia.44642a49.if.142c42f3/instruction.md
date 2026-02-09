# Bug Report

### Describe the bug

When importing Postman collections with raw body content, empty string bodies are not being handled correctly. The importer returns an empty object instead of properly setting up the body structure with the appropriate mime type.

### Reproduction

Import a Postman collection that contains a request with an empty raw body:

```json
{
  "request": {
    "body": {
      "mode": "raw",
      "raw": "",
      "options": {
        "raw": {
          "language": "json"
        }
      }
    }
  }
}
```

The imported request body becomes `{}` instead of having the proper structure with `mimeType` and `text` fields.

### Expected behavior

Even when the raw body is an empty string, the importer should still return a properly structured body object:

```js
{
  mimeType: 'application/json',  // or the detected/provided mime type
  text: ''
}
```

This is causing issues when trying to edit or work with these imported requests, as the body structure is inconsistent with non-empty bodies.

### System Info
- Insomnia version: latest
- Import source: Postman Collection v2

---
Repository: /testbed
