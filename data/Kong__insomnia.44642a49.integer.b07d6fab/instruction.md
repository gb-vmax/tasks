# Bug Report

### Describe the bug

When importing OpenAPI 3.0 specifications, integer parameters are being populated with boolean values (`false`) instead of numeric values in the generated examples. This causes type mismatches and makes the generated requests invalid.

### Reproduction

1. Import an OpenAPI 3.0 spec that contains integer parameters
2. Check the generated parameter examples
3. Notice that integer fields show `false` instead of a numeric value like `0`

Example OpenAPI spec snippet:
```yaml
parameters:
  - name: page
    in: query
    schema:
      type: integer
```

Expected parameter value: `0`
Actual parameter value: `false`

### Expected behavior

Integer type parameters should generate numeric example values (e.g., `0`), not boolean values. The parameter examples should match the declared schema type to ensure valid API requests.

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
