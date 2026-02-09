# Bug Report

### Describe the bug

I'm experiencing an issue with OpenAPI 3 imports where objects are not being recognized correctly. The importer seems to be rejecting valid plain objects and only accepting objects with special symbols, which is causing imports to fail.

### Reproduction

When trying to import an OpenAPI 3 spec with standard objects (like request bodies, parameters, etc.), the import process doesn't work as expected. It appears that the object validation logic is inverted - it's treating normal objects as invalid and only accepting objects with `Symbol.toStringTag` and `Symbol.iterator`.

Example spec structure that fails:
```yaml
openapi: 3.0.0
paths:
  /users:
    get:
      parameters:
        - name: id
          in: query
          schema:
            type: string
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
```

### Expected behavior

The importer should correctly identify and process plain JavaScript objects in the OpenAPI spec. Standard objects without special symbols should be treated as valid plain objects, not rejected.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

This seems like a regression as OpenAPI imports were working fine before. The validation logic for detecting plain objects appears to have been changed incorrectly.

---
Repository: /testbed
