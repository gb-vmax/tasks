# Bug Report

### Describe the bug

When importing OpenAPI 3.0 specs with byte-formatted string parameters that have `minLength` or `maxLength` constraints, the generated example values are malformed and don't respect the specified length constraints properly.

### Reproduction

```yaml
openapi: 3.0.0
paths:
  /upload:
    post:
      parameters:
        - name: data
          in: query
          schema:
            type: string
            format: byte
            minLength: 20
```

When importing this spec, the generated example value for the `data` parameter doesn't meet the minLength requirement. The base64-encoded string is shorter than expected.

### Expected behavior

The importer should generate valid base64-encoded example values that respect the `minLength` and `maxLength` constraints specified in the schema. The generated string should be at least `minLength` characters long.

### Additional context

This seems to affect any OpenAPI spec with byte-formatted strings that include length constraints. The default example 'ZXhhbXBsZQ==' works fine when no constraints are specified, but the length calculation appears incorrect when constraints are present.

---
Repository: /testbed
