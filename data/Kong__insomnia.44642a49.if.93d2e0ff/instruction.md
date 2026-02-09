# Bug Report

### Describe the bug

After importing a Postman collection, the request body is not being displayed correctly. When I import requests with raw body content, the body appears to be missing or empty in Insomnia.

### Reproduction

1. Export a Postman collection that contains requests with raw body content (e.g., JSON payloads)
2. Import the collection into Insomnia
3. Open any request that had a raw body in Postman
4. The request body is empty/not populated

Example of a request that doesn't import correctly:
```json
{
  "name": "Create User",
  "request": {
    "method": "POST",
    "body": {
      "mode": "raw",
      "raw": "{\"name\": \"John Doe\", \"email\": \"john@example.com\"}",
      "options": {
        "raw": {
          "language": "json"
        }
      }
    }
  }
}
```

### Expected behavior

The raw body content from Postman should be imported and displayed in the request body editor in Insomnia. The JSON or other raw content should be preserved.

### System Info

- Insomnia version: latest
- OS: macOS
- Postman collection version: 2.1

This is blocking our team from migrating from Postman to Insomnia. Any help would be appreciated!

---
Repository: /testbed
