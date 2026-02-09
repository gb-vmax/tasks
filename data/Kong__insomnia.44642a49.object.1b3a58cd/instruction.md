# Bug Report

### Describe the bug

When importing Swagger 2.0 specs, the generated example objects for parameters with properties are inconsistent and sometimes include unexpected random properties. The generated examples are non-deterministic, making it difficult to rely on consistent output.

### Reproduction

```js
// Given a Swagger 2.0 parameter with object type:
const parameter = {
  type: 'object',
  properties: {
    name: { type: 'string' },
    email: { type: 'string' },
    age: { type: 'integer' },
    address: { type: 'string' },
    phone: { type: 'string' }
  }
}

// Import the spec multiple times
// Each time, different properties appear in the generated example
// Sometimes you get { name: '', email: '' }
// Other times you get { name: '', age: 0, phone: '' }
```

### Expected behavior

The generated parameter examples should be deterministic and predictable. Ideally, all properties should be included in the example, or at least the same set of properties should be generated consistently each time.

### Additional context

This seems to affect objects with more than 3 properties. The randomness makes testing and debugging really difficult since the output changes on every import. Also noticed that sometimes an extra `additionalProp` field appears even when `additionalProperties` is not explicitly set in the schema.

---
Repository: /testbed
