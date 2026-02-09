# Bug Report

### Describe the bug

When importing Postman collections that contain request items with string URLs (legacy format), the importer is not handling them correctly. The request object is being returned incomplete, missing essential fields like `url`, `method`, `headers`, and `body`.

### Reproduction

Try importing a Postman collection with a request item that has a string URL:

```json
{
  "item": [
    {
      "name": "Simple Request",
      "request": "https://api.example.com/users"
    }
  ]
}
```

After import, the request is created but it's missing:
- URL field (shows as empty)
- HTTP method (should default to GET)
- Headers
- Body
- Authentication settings

### Expected behavior

Even when the request is in string format (legacy Postman format), the importer should create a valid request object with at least:
- The URL properly set
- Default GET method
- Empty headers array
- Empty body

The current implementation just returns an object with only `parentId`, `_id`, `_type`, and `name`, which results in an incomplete/unusable request.

### System Info
- Insomnia version: latest
- Import format: Postman Collection

---
Repository: /testbed
