# Bug Report

### Describe the bug

I'm experiencing an issue with class instance methods not being properly deoptimized. When I have a class with both static and instance methods, the instance methods seem to retain optimizations that should be removed during tree-shaking, leading to incorrect behavior.

### Reproduction

```js
class MyClass {
  static staticMethod() {
    return 'static';
  }
  
  instanceMethod() {
    return 'instance';
  }
  
  constructor() {
    this.value = 42;
  }
}

const instance = new MyClass();
// Instance method calls should trigger deoptimization
instance.instanceMethod();
```

### Expected behavior

Instance methods (non-static, non-constructor methods) should be deoptimized when the class is being processed. Currently it seems like static methods are being incorrectly treated the same as instance methods, or vice versa.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
