# Bug Report

### Describe the bug

I'm experiencing an issue where methods with decorators are being incorrectly tree-shaken from my bundle. The methods are being removed even though they have side effects from their decorators, resulting in runtime errors when the code tries to call these methods.

### Reproduction

```js
class MyClass {
  @sideEffectDecorator
  myMethod() {
    return 'hello';
  }
}

// After bundling, myMethod is removed from the output
// even though the decorator has side effects
```

The decorator should prevent the method from being tree-shaken, but it seems like the bundler is not detecting the side effects properly.

### Expected behavior

Methods with decorators that have side effects should be preserved in the bundle and not removed during tree-shaking.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
