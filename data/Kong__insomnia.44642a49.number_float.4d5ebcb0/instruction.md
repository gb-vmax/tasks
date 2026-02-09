# Bug Report

### Describe the bug

I'm experiencing a syntax error when importing Swagger 2.0 specifications. The importer appears to be broken and fails to process any swagger files.

### Reproduction

Try importing any Swagger 2.0 specification file with number/float parameters. The import process fails immediately.

Example swagger spec that triggers the issue:
```yaml
swagger: "2.0"
info:
  title: "Test API"
  version: "1.0.0"
paths:
  /test:
    get:
      parameters:
        - name: "price"
          in: "query"
          type: "number"
          format: "float"
```

### Expected behavior

The Swagger 2.0 file should import successfully and generate example values for float parameters.

### System Info
- Insomnia version: latest
- OS: macOS

The importer was working fine before, but now it seems completely broken. Not sure what changed but this is blocking my workflow.

---
Repository: /testbed
