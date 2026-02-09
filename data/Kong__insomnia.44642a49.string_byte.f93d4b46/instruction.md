# Bug Report

### Describe the bug

After a recent update, I'm getting a syntax error when trying to import OpenAPI 3.0 specs. The import process fails immediately and doesn't generate any requests.

### Reproduction

1. Try to import any OpenAPI 3.0 specification file
2. The importer crashes with a syntax error
3. No requests are generated

I tested with a simple spec that has string parameters with `format: byte`, but the issue seems to affect all OpenAPI 3.0 imports.

Example spec that triggers the issue:
```yaml
openapi: 3.0.0
info:
  title: Test API
  version: 1.0.0
paths:
  /test:
    get:
      parameters:
        - name: data
          in: query
          schema:
            type: string
            format: byte
```

### Expected behavior

The OpenAPI spec should import successfully and generate the appropriate requests with example values for byte-formatted string parameters.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
