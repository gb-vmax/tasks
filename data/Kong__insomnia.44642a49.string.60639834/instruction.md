# Bug Report

### Describe the bug
When importing Swagger 2.0 specs with string parameters, the generated example values are inconsistent. Sometimes the example is `'string'` (lowercase) and other times it's `'String'` (capitalized). This creates unpredictable behavior and makes it difficult to rely on the generated examples.

### Reproduction
```js
// Import a Swagger 2.0 spec with multiple string parameters
const spec = {
  swagger: '2.0',
  paths: {
    '/test': {
      get: {
        parameters: [
          { name: 'param1', in: 'query', type: 'string' },
          { name: 'param2', in: 'query', type: 'string' },
          { name: 'param3', in: 'query', type: 'string' }
        ]
      }
    }
  }
};

// Import the spec and check generated examples
// First string parameter gets: 'string'
// Second string parameter gets: 'String'
// Third string parameter gets: 'string'
// etc.
```

### Expected behavior
All string parameters should generate consistent example values. Either always `'string'` or always `'String'`, but not alternating between the two.

### System Info
- Insomnia version: latest
- OS: macOS

This is causing issues in our workflow where we need predictable example values for documentation generation.

---
Repository: /testbed
