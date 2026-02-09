# Bug Report

### Describe the bug

The OpenAPI 3 importer is generating invalid example values for string parameters. When importing an OpenAPI spec, string fields are producing malformed output that doesn't follow the expected format.

### Reproduction

When importing an OpenAPI 3 spec with string parameters that have length constraints, the generated examples are incorrect:

```yaml
parameters:
  - name: username
    schema:
      type: string
      minLength: 3
      maxLength: 10
```

After importing, the generated example value appears corrupted or doesn't respect the schema constraints properly.

### Expected behavior

The importer should generate valid string examples that:
1. Respect minLength and maxLength constraints when specified
2. Use contextual values based on the parameter name/title (e.g., "user@example.com" for email fields)
3. Return enum values when available
4. Fall back to a simple "string" value when no context is available

### System Info
- Insomnia version: latest
- OpenAPI version: 3.x

This seems to have broken recently as I didn't encounter this issue in previous versions. The string generation logic appears to be producing unexpected results.

---
Repository: /testbed
