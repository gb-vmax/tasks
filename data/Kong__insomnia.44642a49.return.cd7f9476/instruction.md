# Bug Report

### Describe the bug

When working with API specs that have component schema references, arrays containing nested schemas are not being resolved properly. The array elements that contain `$ref` pointers to component schemas remain unresolved, causing issues when trying to access the actual schema definitions.

### Reproduction

```js
const schemas = {
  User: {
    type: 'object',
    properties: {
      name: { type: 'string' }
    }
  }
};

const spec = {
  items: [
    { $ref: '#/components/schemas/User' },
    { type: 'string' }
  ]
};

const resolved = resolveComponentSchemaRefs(spec, schemas);
// Expected: Array with resolved User schema
// Actual: Array with unresolved $ref objects
```

### Expected behavior

Arrays containing schema references should have those references resolved recursively, so that `$ref` pointers within array elements are replaced with the actual schema definitions from the components section.

### System Info

- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
