# Bug Report

### Describe the bug

I'm encountering a syntax error when importing OpenAPI 3 specifications. The importer appears to be broken and fails to parse the spec file correctly.

### Reproduction

Try importing any OpenAPI 3.0 specification file:

1. Open Insomnia
2. Go to Import/Export
3. Select an OpenAPI 3.0 spec file (any valid spec should trigger this)
4. The import fails with a parsing error

I tested with a simple spec:

```yaml
openapi: 3.0.0
info:
  title: Test API
  version: 1.0.0
paths:
  /users:
    get:
      parameters:
        - name: email
          in: query
          schema:
            type: string
            format: email
```

### Expected behavior

The OpenAPI spec should import successfully and generate the appropriate requests with parameter examples.

### System Info

- Insomnia version: latest
- OS: macOS

This seems to have started recently, possibly after a recent update. The importer was working fine before.

---
Repository: /testbed
