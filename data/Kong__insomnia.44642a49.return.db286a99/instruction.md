# Bug Report

### Describe the bug

When resolving component schema references in API specs, the original properties from the referencing object are being lost. If a schema object contains a `$ref` along with other properties (like `description`, `nullable`, etc.), those additional properties disappear after reference resolution.

### Reproduction

```js
const schemas = {
  User: {
    type: 'object',
    properties: {
      id: { type: 'string' },
      name: { type: 'string' }
    }
  }
};

const schemaWithRef = {
  $ref: '#/components/schemas/User',
  description: 'A user object',
  nullable: true
};

const resolved = resolveComponentSchemaRefs(schemaWithRef, schemas);
// Expected: resolved object should include both the User schema AND the description/nullable properties
// Actual: only the User schema properties are returned, description and nullable are missing
```

### Expected behavior

When a schema object has both a `$ref` and additional properties, the resolved schema should merge the referenced schema with the original properties. The additional properties (like `description`, `nullable`, etc.) should be preserved in the final output.

### System Info

- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
