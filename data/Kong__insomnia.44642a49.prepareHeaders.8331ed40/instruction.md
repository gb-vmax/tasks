# Bug Report

### Describe the bug
After a recent update, the OpenAPI 3 importer is automatically adding an `Accept` header to requests even when one isn't specified in the OpenAPI spec. This is causing issues with APIs that have specific requirements about headers.

### Reproduction
When importing an OpenAPI 3 spec with the following endpoint definition:

```yaml
paths:
  /api/users:
    get:
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
```

The importer now automatically generates and includes an `Accept: application/json` header in the request, even though no Accept header was defined in the parameters.

### Expected behavior
The importer should only include headers that are explicitly defined in the OpenAPI spec parameters. If no Accept header is specified in the spec, it shouldn't be automatically added to the request.

This is breaking backward compatibility with existing specs that rely on default server behavior or have specific header requirements.

---
Repository: /testbed
