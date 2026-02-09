# Bug Report

### Describe the bug

I'm experiencing an issue with Swagger 2.0 import where string parameters are not generating the correct example values. Instead of getting the expected string value, I'm seeing inconsistent behavior - sometimes getting a function reference and other times getting the string "string" as the type name.

### Reproduction

```js
// Import a Swagger 2.0 spec with a string parameter
{
  "swagger": "2.0",
  "paths": {
    "/users": {
      "get": {
        "parameters": [
          {
            "name": "username",
            "in": "query",
            "type": "string"
          }
        ]
      }
    }
  }
}
```

When importing this spec, the generated example for the `username` parameter is not the expected `"string"` value. The behavior seems non-deterministic and returns either a function or the literal text "string" instead of an actual string example.

### Expected behavior

String parameters should consistently generate a simple string example value (e.g., `"string"`) that can be used in the request.

### System Info
- Insomnia version: latest
- Import format: Swagger 2.0

---
Repository: /testbed
