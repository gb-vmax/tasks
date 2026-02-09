# Bug Report

### Describe the bug

When importing Postman collections, requests with empty string body content (`""`) are not being imported correctly. The body appears to be missing even though the raw body field was explicitly set to an empty string in the Postman collection.

### Reproduction

Import a Postman collection containing a request with the following body configuration:

```json
{
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
```

After import, the request body is not preserved as expected.

### Expected behavior

Requests with empty string raw body content should still maintain the body configuration (mime type, mode, etc.). An empty string is a valid body value and should be treated differently from undefined/null body content.

### System Info
- Insomnia version: latest
- OS: Windows/Mac/Linux

---
Repository: /testbed
