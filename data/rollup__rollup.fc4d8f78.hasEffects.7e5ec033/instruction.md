# Bug Report

### Describe the bug

I'm experiencing an issue where logical expressions with side effects are not being handled correctly during tree-shaking. Code that should be preserved because it has side effects is being incorrectly removed from the bundle.

### Reproduction

```js
// Input code
let x = 0;
false && (x = 1);  // This should be removed (no side effects executed)
true && (x = 2);   // This should be kept (side effect will execute)

// Expected: x = 2 should remain in bundle
// Actual: Both expressions are being removed
```

Another example:
```js
let counter = 0;
function increment() {
  counter++;
  return true;
}

// The increment() call has side effects and should be preserved
true && increment();
```

### Expected behavior

When the left side of a logical expression evaluates to a value that means the right side will execute, the right side's side effects should be detected and the expression should be preserved in the output bundle.

For `&&` operator: if left is truthy, right side effects matter
For `||` operator: if left is falsy, right side effects matter

### System Info

- Rollup version: latest
- Node version: 18.x

This seems like a regression in the tree-shaking logic for logical expressions. The bundler is incorrectly determining which branches have effects.

---
Repository: /testbed
