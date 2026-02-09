# Bug Report

### Describe the bug

I'm experiencing unexpected behavior with dead code elimination in block statements. Code that should be removed during tree-shaking is being kept in the bundle, significantly increasing the output size.

### Reproduction

```js
function example() {
  const x = 1;
  return x;
  
  // This code should be eliminated as unreachable
  console.log('unreachable');
  sideEffect();
}
```

When bundling this code, the unreachable statements after the `return` are not being properly eliminated from the output bundle. This seems to affect any code that comes after control flow breaking statements (return, throw, break, continue).

### Expected behavior

Unreachable code following control flow breaking statements should be detected and eliminated during the tree-shaking process. The bundled output should not include these dead code paths.

### Additional context

This appears to have started recently. Previously, the bundler correctly identified and removed unreachable code in block statements. Now it seems like the control flow analysis isn't working as expected.

---
Repository: /testbed
