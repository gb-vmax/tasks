# Bug Report

### Describe the bug

I'm experiencing an issue with optional chaining expressions where side effects are not being properly detected in certain cases. When using optional chaining (`?.`) with expressions that should be considered to have side effects, the bundler seems to be incorrectly evaluating whether effects exist.

### Reproduction

```js
// Example code that triggers the issue
const obj = {
  method: function() {
    console.log('side effect');
    return { nested: 'value' };
  }
};

// Optional chaining with method call
obj.method?.().nested;

// The side effect (console.log) should be preserved
// but it appears to be getting incorrectly tree-shaken
```

### Expected behavior

Optional chaining expressions should correctly identify when the chained expression has side effects. Methods with side effects should not be removed during tree-shaking even when accessed via optional chaining.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. The bundler is treating some expressions with side effects as if they don't have any, leading to unexpected code removal during optimization.

---
Repository: /testbed
