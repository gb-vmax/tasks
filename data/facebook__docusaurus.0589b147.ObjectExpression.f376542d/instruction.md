# Bug Report

### Describe the bug

I'm encountering an issue with object expression generation where the output appears to be incomplete or malformed. When processing object expressions with properties, the generated code seems to be cut off or not properly terminated.

### Reproduction

```js
const objectNode = {
  type: 'ObjectExpression',
  properties: [
    {
      type: 'Property',
      key: { type: 'Identifier', name: 'foo' },
      value: { type: 'Literal', value: 'bar' }
    },
    {
      type: 'Property',
      key: { type: 'Identifier', name: 'baz' },
      value: { type: 'Literal', value: 123 }
    }
  ]
}

// Process this node through the generator
// Expected: properly formatted object with all properties
// Actual: output appears incomplete or malformed
```

### Expected behavior

The generator should produce a complete, properly formatted object expression with all properties correctly rendered and the closing brace in place.

### Additional context

This seems to affect objects with multiple properties. Single-property objects might work fine, but when there are two or more properties, something goes wrong with the iteration or output writing logic.

---
Repository: /testbed
