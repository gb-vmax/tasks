# Bug Report

### Describe the bug
When working with OpenAPI specs that have array schemas with component references, the schema resolution is not working correctly. Only the first item in the array is being returned instead of the full resolved array.

### Reproduction
```js
const schemas = {
  Pet: {
    type: 'object',
    properties: {
      name: { type: 'string' }
    }
  }
};

const arraySchema = [
  { $ref: '#/components/schemas/Pet' },
  { type: 'string' },
  { type: 'number' }
];

const resolved = resolveComponentSchemaRefs(arraySchema, schemas);
// Expected: Array with 3 resolved items
// Actual: Only returns the first resolved item
```

### Expected behavior
When resolving an array of schemas, all items in the array should be resolved and returned as an array. Currently it seems like only the first element is being returned.

### System Info
- Version: latest
- Using API spec resolution with nested component references

---
Repository: /testbed
