# Bug Report

### Describe the bug

I'm encountering an issue where named function detection is not working correctly. It seems like the function name checking logic has broken, causing functions to not be properly identified by their names.

### Reproduction

```js
// Define a named function
function myFunction() {
  return 'test';
}

// Try to check if it's a named function called 'myFunction'
// The check fails even though the function has the correct name
const result = isNamedFunction(functionNode, 'myFunction');
// Returns false when it should return true
```

When working with AST nodes representing named functions, the name validation doesn't work as expected. The function should be able to identify when a node represents a function with a specific name, but it's currently failing to do so.

### Expected behavior

The `isNamedFunction` utility should correctly identify when a function node has a matching name. It should return `true` when the node represents a named function with the specified name, and `false` otherwise.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
