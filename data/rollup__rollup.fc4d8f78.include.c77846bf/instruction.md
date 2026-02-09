# Bug Report

### Describe the bug

I'm encountering an issue where functions with unreachable code after return statements are not being tree-shaken correctly. Code that should be eliminated as dead code is still appearing in the output bundle.

### Reproduction

```js
function example() {
  return 42;
  console.log('This should be removed'); // Dead code
  const x = 10; // This too
}

export { example };
```

When bundling this code, the unreachable statements after the return are still included in the output, even though they can never be executed.

### Expected behavior

Dead code after return statements should be removed from the final bundle. The tree-shaking should recognize that any code following a return statement in the same block is unreachable and eliminate it.

### Additional context

This seems to have started happening recently. Previously, the bundler would correctly identify and remove unreachable code in these scenarios. The issue appears to be related to how control flow is being tracked within function bodies.

---
Repository: /testbed
