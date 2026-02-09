# Bug Report

### Describe the bug

I'm experiencing an issue with code generation where the output is not being returned correctly. When trying to generate code from an AST node, the function returns `undefined` instead of the expected generated code string.

### Reproduction

```js
const ast = {
  type: 'Program',
  body: [
    // ... AST nodes
  ]
}

const result = generate(ast, options)
console.log(result) // undefined - expected: generated code string
```

The `generate()` function seems to process the AST but doesn't return the actual output. This is blocking code generation functionality.

### Expected behavior

The `generate()` function should return a string containing the generated JavaScript code from the provided AST node.

### Additional context

This appears to have started happening recently. The generator is being invoked but the output isn't being captured/returned properly.

---
Repository: /testbed
