# Bug Report

### Describe the bug

I'm encountering an issue with generator functions where setting the `generator` property appears to incorrectly modify the `async` flag instead of the `generator` flag. This causes unexpected behavior when working with generator functions in the AST.

### Reproduction

```js
// Create a function node
const functionNode = createFunctionNode();

// Set generator to true
functionNode.generator = true;

// Expected: generator flag should be set to true
// Actual: async flag gets set to false instead

console.log(functionNode.generator); // Returns unexpected value
```

### Expected behavior

When setting `functionNode.generator = true`, the generator flag should be set to true. The async flag should remain unchanged. Currently it seems like the wrong flag is being modified.

### Additional context

This affects any code that programmatically sets the `generator` property on function nodes. The getter appears to work correctly, but the setter modifies the wrong internal flag.

---
Repository: /testbed
