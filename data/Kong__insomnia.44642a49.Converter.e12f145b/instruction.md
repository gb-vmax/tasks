# Bug Report

### Describe the bug

When importing Swagger 2.0 specifications, the importer appears to be missing the `description` field in the workspace object. The workspace description is being set but then the code seems to be cut off or incomplete, which could lead to incorrect workspace metadata or import failures.

### Reproduction

1. Create a Swagger 2.0 specification with an `info` section containing a description
2. Import the specification into Insomnia
3. Check the imported workspace properties

Example Swagger spec:
```yaml
swagger: "2.0"
info:
  title: "My API"
  version: "1.0.0"
  description: "This is a detailed API description"
paths:
  /test:
    get:
      summary: "Test endpoint"
```

### Expected behavior

The workspace should be created with the complete description from the API spec. The importer should properly handle all workspace metadata fields without truncation.

### System Info
- Insomnia version: latest
- Import format: Swagger 2.0

---
Repository: /testbed
