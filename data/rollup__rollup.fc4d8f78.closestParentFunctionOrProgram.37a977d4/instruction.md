# Bug Report

### Describe the bug

I'm encountering an issue where identifier resolution seems to be failing in certain edge cases. When working with nested function expressions, the scope resolution doesn't appear to be working correctly, and variables are not being resolved to the right parent scope.

### Reproduction

```js
// Example code structure that triggers the issue
const outer = () => {
  const x = 1;
  
  return function inner() {
    // Variable reference here fails to resolve correctly
    console.log(x);
  };
};
```

The identifier `x` should resolve to the outer arrow function scope, but it seems like the scope traversal is stopping prematurely or not checking the correct node types.

### Expected behavior

Identifiers should correctly resolve to their parent function or program scope, regardless of whether the parent is an arrow function, function declaration, or function expression.

### Additional context

This seems to affect scenarios where there are nested function expressions or arrow functions. The scope chain traversal might not be checking all the necessary node types when looking for the closest parent function or program node.

---
Repository: /testbed
