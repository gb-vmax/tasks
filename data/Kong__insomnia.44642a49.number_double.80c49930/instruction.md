# Bug Report

### Describe the bug

After a recent update, OpenAPI 3.0 spec imports are failing with a syntax error. It looks like there's a malformed code structure in the parameter example generation logic.

### Reproduction

Try importing any OpenAPI 3.0 specification file that contains numeric parameters with schema definitions. The import process throws a syntax error and fails to complete.

Steps to reproduce:
1. Create an OpenAPI 3.0 spec with a numeric parameter (double type)
2. Attempt to import the spec into Insomnia
3. Import fails with a parsing/syntax error

Example spec snippet that triggers the issue:
```yaml
parameters:
  - name: amount
    in: query
    schema:
      type: number
      format: double
      minimum: 0
      maximum: 100
```

### Expected behavior

The OpenAPI 3.0 spec should import successfully and generate appropriate example values for numeric parameters with double format.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started happening very recently - imports were working fine before. The error suggests there's a syntax issue in the importer code itself.

---
Repository: /testbed
