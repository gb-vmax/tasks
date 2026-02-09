# Bug Report

### Describe the bug

I'm experiencing an issue with decorators where side effects are not being properly detected. When a decorator expression has side effects, they seem to be ignored in certain cases, leading to incorrect tree-shaking behavior.

### Reproduction

```js
class MyClass {
  @sideEffectDecorator()
  method() {
    return 'test';
  }
}
```

When the decorator function `sideEffectDecorator()` has side effects (like logging, modifying global state, or performing I/O), these effects are not being tracked correctly. This causes the decorator to potentially be removed during bundling even though it should be preserved.

### Expected behavior

Decorators with side effects should always be included in the bundle. The bundler should detect when a decorator expression has side effects and preserve it accordingly.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
