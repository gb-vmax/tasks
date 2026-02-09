# Bug Report

### Describe the bug

I'm experiencing an issue with OpenAPI 3 import where string parameters with `minLength` and `maxLength` constraints are not generating example values that respect these constraints. The generated examples are always just the default "string" value regardless of the length requirements specified in the schema.

### Reproduction

Given an OpenAPI 3 spec with a string parameter like this:

```yaml
parameters:
  - name: userId
    in: query
    schema:
      type: string
      minLength: 10
      maxLength: 20
```

When importing this spec, the generated example value is just "string" (6 characters), which doesn't satisfy the minLength constraint of 10 characters.

Similarly, for a parameter with:
```yaml
schema:
  type: string
  minLength: 50
```

The example should be at least 50 characters long, but it's still just "string".

### Expected behavior

The importer should generate example values that respect the `minLength` and `maxLength` constraints defined in the schema. For example:
- If `minLength: 10`, the example should be at least 10 characters
- If `maxLength: 5`, the example should be at most 5 characters
- If both are specified, the example should fall within that range

This would make the imported requests immediately usable without having to manually adjust parameter values to meet validation requirements.

### System Info
- Insomnia version: latest
- Import format: OpenAPI 3.0

---
Repository: /testbed
