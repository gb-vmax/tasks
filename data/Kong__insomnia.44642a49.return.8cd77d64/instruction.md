# Bug Report

### Describe the bug

When resolving OpenAPI schema references with nested components, the resolved schema objects are not being properly dereferenced. If a schema contains a `$ref` that points to another schema in `#/components/schemas/`, the reference object itself is returned instead of the resolved schema content.

### Reproduction

```js
const schemas = {
  User: {
    type: 'object',
    properties: {
      id: { type: 'string' },
      name: { type: 'string' }
    }
  },
  UserResponse: {
    type: 'object',
    properties: {
      user: { $ref: '#/components/schemas/User' }
    }
  }
};

const resolved = resolveComponentSchemaRefs(schemas.UserResponse, schemas);
// Expected: user property should contain the full User schema
// Actual: user property contains the schema object with $ref still present
```

### Expected behavior

When a schema contains a `$ref` to another component schema, the function should recursively resolve the reference and return the actual schema definition, not just the schema object from the components. The resolved output should have all `$ref` properties replaced with their actual schema definitions.

### Additional context

This affects API spec parsing where schemas reference other schemas. The dereferencing doesn't work as expected, which can cause issues downstream when trying to generate documentation or validate requests against the schema.

---
Repository: /testbed
