# Bug Report

### Describe the bug

After a recent update, the OpenAPI 3 importer is generating malformed example data for number fields with `float` format. The generated examples appear to be producing syntax errors or invalid structure instead of proper float values.

### Reproduction

When importing an OpenAPI 3 spec with a number field that has format `float`, the importer fails to generate valid example data:

```yaml
components:
  schemas:
    Product:
      type: object
      properties:
        price:
          type: number
          format: float
          minimum: 0
          maximum: 1000
```

The importer seems to be breaking when trying to generate example values for this field.

### Expected behavior

The importer should generate a valid float example value (e.g., `0.0` or a random float within constraints if min/max are specified).

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
