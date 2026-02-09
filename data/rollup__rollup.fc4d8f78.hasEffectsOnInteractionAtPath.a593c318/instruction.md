# Bug Report

### Describe the bug

I'm experiencing an issue where accessing properties on the `arguments` object is being treated as having side effects when it shouldn't. This seems to be causing unnecessary code to be included in the bundle that should be tree-shaken away.

### Reproduction

```js
function myFunction() {
  // Simple property access on arguments
  const firstArg = arguments[0];
  const length = arguments.length;
  
  // These accesses should not be considered as having effects
  return firstArg;
}
```

When bundling code that accesses `arguments` properties, the behavior seems incorrect - simple reads from the `arguments` object are being flagged as having side effects, preventing proper tree-shaking and dead code elimination.

### Expected behavior

Accessing properties on the `arguments` object (like `arguments[0]` or `arguments.length`) should be treated as a pure read operation without side effects. Only mutations or method calls should be considered as having effects.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
