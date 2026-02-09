# Bug Report

### Describe the bug

I'm experiencing an issue where property assignments on bound member expressions aren't being properly tracked for tree-shaking. When assigning to properties of objects that are bound in the scope, the bundler is incorrectly removing code that should be kept because it has side effects.

### Reproduction

```js
// input.js
const obj = {
  get value() {
    console.log('side effect');
    return this._value;
  },
  set value(v) {
    console.log('setter side effect');
    this._value = v;
  }
};

// This assignment should be kept due to setter side effects
obj.value = 42;

export { obj };
```

When bundling this code with tree-shaking enabled, the assignment `obj.value = 42` is being incorrectly removed even though the setter has observable side effects. The bundled output is missing the setter call entirely.

### Expected behavior

The assignment should be preserved in the output since the property setter has side effects. The tree-shaker should detect that bound member expressions can have side effects through getters/setters and keep the assignment.

### System Info
- Rollup version: latest
- Node version: 18.x
- treeshake.propertyReadSideEffects: true

---
Repository: /testbed
