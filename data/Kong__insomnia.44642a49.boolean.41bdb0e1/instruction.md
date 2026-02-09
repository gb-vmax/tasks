# Bug Report

### Describe the bug
When importing Swagger 2 specs with boolean parameters, the generated examples are not deterministic. The boolean values appear to be random instead of consistently using the same value, which makes it difficult to have reproducible API documentation and test cases.

### Reproduction
```js
// Import a Swagger 2 spec with a boolean parameter
const spec = {
  paths: {
    '/api/test': {
      get: {
        parameters: [{
          name: 'enabled',
          in: 'query',
          type: 'boolean'
        }]
      }
    }
  }
}

// Import the spec multiple times
// Expected: Same boolean value each time
// Actual: Random true/false values
```

### Expected behavior
Boolean parameters should generate consistent example values across imports. Ideally they should default to `true` or use the `example`/`default` field if provided in the spec.

### Additional context
This makes it hard to create consistent documentation and example requests. Every time the spec is re-imported, the boolean values change randomly, which is confusing for users and breaks reproducibility.

---
Repository: /testbed
