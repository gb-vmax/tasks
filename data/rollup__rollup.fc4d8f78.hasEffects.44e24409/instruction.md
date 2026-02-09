# Bug Report

### Describe the bug

I'm experiencing an issue where class method definitions with decorators are being incorrectly tree-shaken/removed from the bundle even when they have side effects. This seems to affect methods that have decorators but no direct side effects in the method body itself.

### Reproduction

```js
class MyClass {
  @decorator
  myMethod() {
    // Method gets removed even though decorator might have side effects
  }
}
```

The method `myMethod` is being removed from the output bundle despite having a decorator that could have side effects. This appears to be a regression in the tree-shaking logic.

### Expected behavior

Methods with decorators should be preserved in the bundle if the decorators have side effects, regardless of whether the method body itself has side effects. The tree-shaking should check both the decorators AND the method body, not just one or the other.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
