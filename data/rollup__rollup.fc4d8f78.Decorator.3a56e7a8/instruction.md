# Bug Report

### Describe the bug

Decorators are not being properly evaluated for side effects during tree-shaking. When a decorator expression has side effects (like function calls or property access that could trigger getters), these effects are being ignored and the code is incorrectly removed during the build process.

### Reproduction

```js
let sideEffectCount = 0;

function trackDecorator(target) {
  sideEffectCount++;
  console.log('Decorator executed');
  return target;
}

@trackDecorator
class MyClass {
  method() {}
}

// Expected: sideEffectCount should be 1 and console should log
// Actual: decorator is tree-shaken away, sideEffectCount stays 0
```

Another example with property access:

```js
const config = {
  get register() {
    console.log('Registering class');
    return (target) => target;
  }
};

@config.register
class Component {}

// The property getter should be called, but it's being removed
```

### Expected behavior

Decorator expressions should be evaluated even if the decorated class isn't directly used, because the decorator itself might have important side effects. The tree-shaker should preserve decorators when their expressions could have side effects.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
