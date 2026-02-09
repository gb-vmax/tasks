# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking where property access on member expressions is not being properly analyzed for side effects. It seems like the bundler is incorrectly removing code that should be kept because it's not detecting side effects from property reads correctly.

### Reproduction

```js
// input.js
const obj = {
  get value() {
    console.log('side effect!');
    return 42;
  }
};

const result = obj.value;
export { result };
```

When bundling this code with tree-shaking enabled and `propertyReadSideEffects` configured, the getter's side effect is not being preserved as expected. The property access seems to be treated as if it has no side effects even when it clearly does.

### Expected behavior

The bundler should correctly identify that accessing `obj.value` has side effects (the console.log in the getter) and should preserve this code during tree-shaking. The property read side effects analysis should properly check the interaction at the correct path.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This seems to have started happening recently. The tree-shaking is being too aggressive and removing code that has observable side effects.

---
Repository: /testbed
