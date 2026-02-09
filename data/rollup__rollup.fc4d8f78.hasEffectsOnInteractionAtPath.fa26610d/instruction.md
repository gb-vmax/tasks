# Bug Report

### Describe the bug

I'm experiencing an issue where `new` expressions are being incorrectly tree-shaken/removed from the bundle even when they have side effects. The constructor call should be preserved but it's getting eliminated during the build process.

### Reproduction

```js
class MyClass {
  constructor() {
    console.log('Constructor called - this should appear!');
    // Side effect that should be preserved
    globalThis.initialized = true;
  }
}

// This new expression is being removed even though it has side effects
new MyClass();

export default function() {
  return 'test';
}
```

After bundling, the `new MyClass()` call is completely removed from the output, which means the constructor side effects never execute.

### Expected behavior

The `new` expression should be preserved in the bundle since instantiating the class triggers side effects through the constructor. The constructor logs to console and modifies global state, so it shouldn't be tree-shaken away.

### Additional context

This seems to have started happening recently. Previously, constructor calls with side effects were correctly retained in the bundle. Now they're being treated as if they have no effects and are being removed during optimization.

---
Repository: /testbed
