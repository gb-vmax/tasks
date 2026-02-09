# Bug Report

### Describe the bug

I'm experiencing an issue with resolving schema references in OpenAPI specs. When a schema contains a `$ref` that points to something other than `#/components/schemas/`, the reference resolution gets stuck in an infinite loop and causes the application to hang.

### Reproduction

```js
const schemas = {
  User: {
    type: 'object',
    properties: {
      id: { type: 'string' },
      address: { $ref: '#/definitions/Address' }  // Note: #/definitions, not #/components/schemas
    }
  }
};

// This causes infinite recursion
resolveComponentSchemaRefs(schemas.User, schemas);
```

### Expected behavior

The function should handle references that don't match the `#/components/schemas/` pattern gracefully, either by leaving them unresolved or handling them appropriately without causing infinite recursion.

### System Info
- Insomnia version: latest
- OS: macOS

The issue seems to be that when a `$ref` doesn't start with `#/components/schemas/`, the replacement operation returns the original ref unchanged, which then gets passed back into the recursive function indefinitely.

---
Repository: /testbed
