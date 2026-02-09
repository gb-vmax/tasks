# Bug Report

### Describe the bug

When importing Swagger 2.0 specs with `string_byte` format parameters, the generated example values don't respect the parameter's `example`, `default`, `minLength`, or `maxLength` properties. The importer always returns the same hardcoded base64 string `'ZXhhbXBsZQ=='` regardless of what's defined in the spec.

### Reproduction

Given a Swagger 2.0 spec with a parameter like:

```yaml
parameters:
  - name: data
    in: body
    schema:
      type: string
      format: byte
      example: "dGVzdA=="
      minLength: 20
      maxLength: 50
```

The imported request will use `'ZXhhbXBsZQ=='` instead of the provided example or generating a value that respects the length constraints.

### Expected behavior

The importer should:
1. Use the `example` value if it's a valid base64 string
2. Fall back to the `default` value if provided and valid
3. Generate a base64 string that respects `minLength`/`maxLength` constraints
4. Only use the hardcoded fallback when none of the above are available

### System Info
- Insomnia version: latest
- Import format: Swagger 2.0

---
Repository: /testbed
