# Bug Report

### Describe the bug

After a recent update, the API spec schema resolution is completely broken. When trying to load OpenAPI specifications, the application fails to properly resolve component references and the schema resolution function appears to have duplicate/malformed code.

### Reproduction

When loading any OpenAPI spec that uses `$ref` to reference components, the schema resolution fails. For example:

```yaml
components:
  schemas:
    User:
      type: object
      properties:
        name:
          type: string
    UserList:
      type: array
      items:
        $ref: '#/components/schemas/User'
```

Trying to resolve references in this spec causes the application to behave unexpectedly - the function seems to have corrupted code with duplicate function definitions overlapping each other.

### Expected behavior

The `resolveComponentSchemaRefs` function should properly resolve all component references in the OpenAPI spec, including:
- Schema references
- Parameter references  
- Response references
- Request body references
- Other component types

The function should recursively resolve nested references and return the fully resolved schema object.

### System Info

- Insomnia version: latest
- The issue appears in the `packages/insomnia/src/common/api-specs.ts` file
- Affects all API spec loading functionality

The code in the file looks malformed with what appears to be a merge conflict or copy-paste error where the function definition is duplicated and the original logic is incomplete.

---
Repository: /testbed
