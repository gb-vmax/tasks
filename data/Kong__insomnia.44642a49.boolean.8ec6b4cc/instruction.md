# Bug Report

### Describe the bug

When importing OpenAPI 3 specifications, boolean parameters are always generated with a `true` value, regardless of any schema definitions like `default`, `example`, or `enum` values that might specify otherwise.

### Reproduction

Given an OpenAPI 3 spec with a boolean parameter that has a default value:

```yaml
parameters:
  - name: isActive
    in: query
    schema:
      type: boolean
      default: false
```

When importing this spec, the generated request uses `true` instead of the specified `false` default value.

Similarly, if the schema defines an example or enum:

```yaml
schema:
  type: boolean
  example: false
```

or

```yaml
schema:
  type: boolean
  enum: [false]
```

The importer still generates `true` for all boolean parameters.

### Expected behavior

Boolean parameters should respect the schema definitions in this order of priority:
1. Use `default` value if specified
2. Use `example` value if specified  
3. Use first value from `enum` if specified
4. Only fallback to `true` if none of the above are defined

This would make the generated requests more accurate to the API specification and provide better default values for testing.

---
Repository: /testbed
