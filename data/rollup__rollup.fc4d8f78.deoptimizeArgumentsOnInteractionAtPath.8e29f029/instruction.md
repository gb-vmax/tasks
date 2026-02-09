# Bug Report

### Describe the bug

I'm encountering an issue where method calls on arrays are not being properly tracked for side effects. It appears that mutations to array elements through methods are not being deoptimized correctly, which can lead to incorrect tree-shaking behavior.

### Reproduction

```js
const arr = [1, 2, 3];
const callback = (item) => {
  // Side effect that should be preserved
  console.log(item);
};

// This call should deoptimize the callback argument
arr.forEach(callback);

// The callback's side effects may be incorrectly removed during optimization
```

When using array methods like `forEach`, `map`, or `filter` that accept callback functions, the arguments passed to these callbacks aren't being properly marked as having potential side effects. This can cause the bundler to incorrectly remove code that should be preserved.

### Expected behavior

Arguments passed to array method callbacks should be deoptimized to ensure their side effects are preserved during the optimization phase. The bundler should treat these arguments conservatively and not remove them during tree-shaking.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
