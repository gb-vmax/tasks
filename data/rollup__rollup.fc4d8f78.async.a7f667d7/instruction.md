# Bug Report

### Describe the bug

I'm encountering an issue with async function detection in my code. When I set or update the `async` property on function nodes, the behavior is completely inverted - async functions are being treated as sync and vice versa.

### Reproduction

```js
// Create a function node
const functionNode = new FunctionBase();

// Set it as async
functionNode.async = true;

// Check the async property
console.log(functionNode.async); // Expected: true, Actual: false

// Try setting it to false
functionNode.async = false;
console.log(functionNode.async); // Expected: false, Actual: true
```

### Expected behavior

When setting `async = true`, the function should be marked as async and `async` getter should return `true`. When setting `async = false`, it should be marked as sync and return `false`.

Currently it's doing the opposite - setting `true` makes it return `false` and setting `false` makes it return `true`.

### Additional context

This seems to affect AST parsing and function analysis. Any code that relies on checking whether a function is async or not will get incorrect results.

---
Repository: /testbed
