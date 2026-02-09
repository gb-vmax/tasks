# Bug Report

### Describe the bug

When importing Swagger 2.0 specifications, the parameter example generation for string types doesn't respect the `enum`, `pattern`, `minLength`, or `maxLength` properties defined in the parameter schema. All string parameters are being generated with the generic value `'string'` regardless of their constraints.

### Reproduction

Given a Swagger 2.0 spec with parameters like:

```yaml
parameters:
  - name: status
    in: query
    type: string
    enum: ["active", "inactive", "pending"]
  
  - name: uuid
    in: query
    type: string
    pattern: "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"
  
  - name: code
    in: query
    type: string
    minLength: 10
    maxLength: 20
```

When importing this spec, all three parameters get the example value `'string'` instead of:
- `'active'` (first enum value)
- A valid UUID format
- A string between 10-20 characters

### Expected behavior

The importer should generate realistic example values based on the parameter constraints:
- If `enum` is present, use the first enum value
- If `pattern` is present, generate a value matching common patterns (UUID, phone, URL, etc.)
- If `minLength`/`maxLength` are present, generate a string of appropriate length

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

This makes imported API specs less useful since the example values don't reflect the actual parameter requirements.

---
Repository: /testbed
