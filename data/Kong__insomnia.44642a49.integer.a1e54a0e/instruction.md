# Bug Report

### Describe the bug

When importing OpenAPI 3.0 specs, the importer crashes or produces incomplete results when processing integer schema parameters. It appears that something went wrong with the integer type generation logic, causing the import process to fail silently or produce malformed requests.

### Reproduction

Try importing an OpenAPI 3.0 specification that contains integer parameters with constraints like:

```yaml
parameters:
  - name: page
    in: query
    schema:
      type: integer
      minimum: 1
      maximum: 100
      multipleOf: 5
```

Or with enum values:

```yaml
parameters:
  - name: status
    in: query
    schema:
      type: integer
      enum: [1, 2, 3]
```

The import process either fails to complete or the generated requests are missing parameter examples/values.

### Expected behavior

The importer should successfully process integer schemas with various constraints (minimum, maximum, multipleOf, enum) and generate appropriate example values for the imported requests.

### System Info
- Insomnia version: latest
- Platform: N/A

This seems to have started happening recently, possibly after some changes to the OpenAPI 3 importer code.

---
Repository: /testbed
