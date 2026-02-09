# Bug Report

### Describe the bug

When importing OpenAPI 3 specs, the Accept header is being added to requests even when an Accept header already exists in the parameter definitions. This causes duplicate Accept headers with potentially conflicting values.

### Reproduction

Given an OpenAPI 3 spec with:
```yaml
paths:
  /api/resource:
    get:
      parameters:
        - name: accept
          in: header
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                type: object
```

When importing this spec, the generated request will have two Accept headers - one from the parameter definition and one automatically added based on the response content type.

### Expected behavior

The importer should respect existing Accept headers (case-insensitive) and not add a duplicate. If an Accept header is already defined in the parameters, it should not be overwritten or duplicated.

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
