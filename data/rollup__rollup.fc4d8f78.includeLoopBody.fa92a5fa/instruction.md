# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking in loop statements. Code that should be removed as dead code after a `break` statement inside a loop is incorrectly being included in the bundle.

### Reproduction

```js
function test() {
  while (true) {
    break;
    console.log('This should be tree-shaken');
    sideEffect();
  }
  return 'done';
}
```

The code after the `break` statement is unreachable and should be eliminated during the tree-shaking process, but it's still appearing in the output bundle.

### Expected behavior

Unreachable code following a `break` statement in loops should be properly detected and removed from the final bundle. The tree-shaking optimization should recognize that statements after `break` will never execute.

### Additional context

This seems to affect various loop types (while, for, do-while). The issue appears to be related to how the broken flow analysis handles loop bodies.

---
Repository: /testbed
