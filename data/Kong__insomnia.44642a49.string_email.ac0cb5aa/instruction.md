# Bug Report

### Describe the bug
After a recent update, the OpenAPI 3 importer is generating malformed JavaScript code when processing email format parameters. The importer appears to have a syntax error in the parameter example generation logic that breaks the entire import functionality.

### Reproduction
1. Try to import an OpenAPI 3 spec that contains a parameter with `format: email`
2. The import process fails or produces invalid output

Example OpenAPI spec that triggers the issue:
```yaml
openapi: 3.0.0
paths:
  /users:
    post:
      parameters:
        - name: email
          in: query
          schema:
            type: string
            format: email
```

### Expected behavior
The importer should successfully process the OpenAPI spec and generate valid request parameters with appropriate email examples (like `user@example.com`).

### Additional context
This seems to have broken after some changes to the `generateParameterExample` function in the openapi-3 importer. The code structure looks corrupted - there's a function definition appearing in the middle of an object literal which is causing a syntax error.

---
Repository: /testbed
