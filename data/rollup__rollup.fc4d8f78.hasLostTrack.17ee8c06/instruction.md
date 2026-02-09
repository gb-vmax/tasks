# Bug Report

### Describe the bug

I'm experiencing an issue where object property tracking appears to be completely broken. When accessing properties on objects, the bundler seems to incorrectly assume that tracking has been lost even when it hasn't, leading to overly conservative tree-shaking behavior.

### Reproduction

```js
const obj = {
  foo: 'bar',
  nested: {
    value: 42
  }
};

// Accessing properties
console.log(obj.foo);
console.log(obj.nested.value);

// These accesses should be tracked properly, but they're not
```

After bundling, the code behaves as if property tracking is always lost, which causes issues with dead code elimination and side effect detection.

### Expected behavior

The object entity should correctly track property accesses and only mark tracking as lost when it actually is (e.g., after spreading, dynamic property access, etc.). Normal property accesses should maintain proper tracking state.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. The bundler is being overly conservative about what it considers "tracked" vs "untracked" object accesses.

---
Repository: /testbed
