# Bug Report

### Describe the bug

When resolving OpenAPI schema references using `$ref`, the function is not properly returning the resolved schema. Instead of returning the dereferenced schema object, it appears to be returning the original object with the `$ref` still present.

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

const obj = {
  $ref: '#/components/schemas/User'
};

const resolved = resolveComponentSchemaRefs(obj, schemas);
// Expected: { type: 'object', properties: { name: { type: 'string' } } }
// Actual: { $ref: '#/components/schemas/User' }
```

### Expected behavior

When an object contains a `$ref` property pointing to a schema in the components, the function should resolve and return the actual schema definition, not the original reference object.

### Additional context

This is affecting API spec parsing where schema references need to be properly dereferenced to display correct type information in the UI. The reference should be followed and the target schema should be returned.

---
Repository: /testbed
