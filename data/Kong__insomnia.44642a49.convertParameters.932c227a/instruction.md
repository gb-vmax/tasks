# Bug Report

### Describe the bug

When importing OpenAPI 3.x specifications, parameters with `example` values defined at the parameter level are being ignored. The importer only seems to use the `example` from the schema object or falls back to generating examples, even when an explicit `example` is provided directly on the parameter.

### Reproduction

Given an OpenAPI spec like this:

```yaml
parameters:
  - name: userId
    in: path
    required: true
    example: "12345"
    schema:
      type: string
      example: "abc"
```

After importing, the parameter value is set to "abc" (from schema.example) or a generated value, instead of using "12345" from the parameter's `example` field.

### Expected behavior

The importer should prioritize the `example` value defined directly on the parameter object over the schema's example. According to the OpenAPI 3.x spec, parameter-level examples should take precedence.

Expected parameter value: `"12345"`
Actual parameter value: `"abc"` or generated value

### System Info
- Insomnia version: latest
- OpenAPI spec version: 3.0.x

---
Repository: /testbed
