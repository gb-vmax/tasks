# Bug Report

### Describe the bug

When importing OpenAPI 3.0 specs with byte-formatted strings that have `minLength` or `maxLength` constraints, the generated example values don't respect these length requirements. The importer always generates the same hardcoded base64 string `'ZXhhbXBsZQ=='` regardless of the schema constraints.

### Reproduction

```yaml
openapi: 3.0.0
paths:
  /upload:
    post:
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                data:
                  type: string
                  format: byte
                  minLength: 100
```

When importing this spec, the generated example for the `data` field is always `'ZXhhbXBsZQ=='` (which decodes to only 7 bytes), even though the schema specifies a minimum length of 100.

### Expected behavior

The importer should generate base64-encoded example values that respect the `minLength` and `maxLength` constraints defined in the schema. For example, if `minLength: 100` is specified, the generated base64 string should decode to at least 100 bytes.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
