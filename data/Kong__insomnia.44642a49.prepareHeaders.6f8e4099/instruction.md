# Bug Report

### Describe the bug

After a recent update, I'm seeing duplicate headers being generated when importing OpenAPI 3 specs. The importer now adds an `Accept` header based on response content types, but it doesn't properly handle cases where an `Accept` header already exists in the spec's parameter definitions.

### Reproduction

When importing an OpenAPI 3 spec with the following structure:

```yaml
paths:
  /api/users:
    get:
      parameters:
        - name: Accept
          in: header
          schema:
            type: string
          example: "application/json"
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
```

The imported request ends up with duplicate `Accept` headers - one from the parameters definition and one auto-generated from the response content types.

### Expected behavior

The importer should detect existing `Accept` headers and either:
1. Not add a duplicate header, or
2. Merge the values intelligently

Currently getting requests with malformed headers that cause issues when sending.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
