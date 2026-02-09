# Bug Report

### Describe the bug

After a recent update, OpenAPI 3 import is failing with a syntax error. The importer seems to have a malformed code structure that prevents it from working correctly.

### Reproduction

1. Try to import an OpenAPI 3 specification file
2. The import process fails immediately
3. Console shows syntax/parsing errors related to the openapi-3 importer

```js
// Any OpenAPI 3 spec import will fail, for example:
{
  "openapi": "3.0.0",
  "paths": {
    "/test": {
      "get": {
        "parameters": [{
          "name": "value",
          "in": "query",
          "schema": {
            "type": "number",
            "format": "float"
          }
        }]
      }
    }
  }
}
```

### Expected behavior

The OpenAPI 3 specification should import successfully without syntax errors. The importer should be able to parse and process the spec file correctly.

### System Info
- Insomnia version: latest
- OS: macOS

This appears to be a regression as OpenAPI 3 imports were working fine in the previous version. The issue seems to be in the parameter example generation code.

---
Repository: /testbed
