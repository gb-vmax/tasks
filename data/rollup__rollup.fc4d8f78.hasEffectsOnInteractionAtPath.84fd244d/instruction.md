# Bug Report

### Describe the bug

I'm encountering an issue where constructor calls are being incorrectly tracked in the side effects analysis. When instantiating objects with `new`, the bundler seems to be confusing the tracking context between regular function calls and constructor invocations.

### Reproduction

```js
class MyClass {
  constructor() {
    this.value = 42;
  }
}

// This should be tracked as a constructor call
const instance = new MyClass();

// But the tracking appears to be swapped somehow
// Leading to incorrect tree-shaking decisions
```

The problem manifests when the bundler analyzes whether certain code can be safely removed. Constructor calls are being treated as regular calls and vice versa, which causes the tree-shaking to make incorrect assumptions about side effects.

### Expected behavior

Constructor calls (with `new`) should be tracked separately from regular function calls. The context used for tracking `new` expressions should be `context.instantiated`, while regular calls should use `context.called`.

### System Info
- Rollup version: latest
- Node version: 18.x

This appears to be affecting the dead code elimination pass. Code that should be retained is being removed, or code that could be safely removed is being kept.

---
Repository: /testbed
