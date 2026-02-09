# Bug Report

### Describe the bug

When importing Postman collections with raw request bodies that have an empty string value, the import process fails to properly handle the body data. The imported request ends up with missing body configuration instead of having an empty raw body with the appropriate mime type.

### Reproduction

1. Export a Postman collection that contains a request with a raw body set to an empty string
2. Import this collection into Insomnia
3. Check the imported request's body configuration

Expected: The request should have a body object with the mime type preserved (e.g., `{ mimeType: 'text/plain', text: '' }`)

Actual: The body configuration is completely missing (returns an empty object `{}`)

### Steps to reproduce

```js
// Example Postman collection structure
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

When importing this, the body data is lost entirely instead of being preserved as an empty body with the correct mime type.

### Expected behavior

Empty raw bodies should still be imported with their mime type information intact. The importer should return a proper body object even when the content is empty, so that the body mode and type are preserved from the original Postman collection.

### Additional context

This affects workflows where users intentionally have empty request bodies (like certain GET or DELETE requests) but want to maintain the body configuration for later use.

---
Repository: /testbed
