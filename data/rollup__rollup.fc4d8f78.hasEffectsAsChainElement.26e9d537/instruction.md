# Bug Report

### Describe the bug

I'm experiencing an issue with optional chaining in call expressions where the bundler is incorrectly removing code that should be included. When using optional chaining with a function call (e.g., `foo?.()`), the bundler appears to be treating the call as having no side effects even when the callee itself has side effects.

### Reproduction

```js
// Input code
const obj = {
  method() {
    console.log('This should execute');
    return 42;
  }
};

obj.method?.();

// Another example
function maybeCall(fn) {
  fn?.();
}

maybeCall(() => {
  console.log('Side effect here');
});
```

### Expected behavior

The optional chained calls should be preserved in the output when they have side effects. The callee's side effects should be properly detected and the code should not be tree-shaken away.

### Actual behavior

The bundler seems to be incorrectly skipping these calls during the tree-shaking phase, even though they contain side effects that should prevent removal.

### System Info

- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. The code with optional chaining calls is being removed from the bundle when it shouldn't be.

---
Repository: /testbed
