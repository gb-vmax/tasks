# Bug Report

### Describe the bug

I'm experiencing an issue where `new` expressions are being included multiple times in the output bundle, causing code duplication. It seems like the inclusion logic is running more than once for the same node.

### Reproduction

```js
// input.js
class MyClass {
  constructor(value) {
    this.value = value;
  }
}

export const instance = new MyClass(42);
```

When bundling this code, the `new MyClass(42)` expression and its arguments appear to be processed/included multiple times, leading to unexpected behavior in the generated output.

### Expected behavior

Each `new` expression should only be included once in the bundle. The callee and arguments should be processed exactly one time during the inclusion phase.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
