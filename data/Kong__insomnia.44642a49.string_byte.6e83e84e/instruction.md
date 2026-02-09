# Bug Report

### Describe the bug

When importing OpenAPI 3 specs with `string_byte` type parameters that have `minLength` or `maxLength` constraints, the generated example values don't respect these length constraints. The importer always generates the same fixed base64 string regardless of the schema's length requirements.

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
            minLength: 50
```

When importing this spec, the generated example is still the default `ZXhhbXBsZQ==` (which is only 12 characters) instead of a base64 string that meets the 50 character minimum length requirement.

### Expected behavior

The importer should generate base64 example strings that respect the `minLength` and `maxLength` constraints defined in the OpenAPI schema. For example, if `minLength: 50` is specified, the generated base64 string should be at least 50 characters long.

### Additional context

This affects API testing workflows where length validation is important. Currently have to manually edit the generated examples to match the schema constraints.

---
Repository: /testbed
