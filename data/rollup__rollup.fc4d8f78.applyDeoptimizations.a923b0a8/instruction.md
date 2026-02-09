# Bug Report

### Describe the bug

I'm experiencing an issue with class methods where instance methods are not being properly handled during deoptimization. It appears that instance methods are being deoptimized when they shouldn't be, which is causing unexpected behavior in my code.

### Reproduction

```js
class MyClass {
  instanceMethod() {
    return this.value;
  }
  
  static staticMethod() {
    return 'static';
  }
  
  constructor() {
    this.value = 42;
  }
}

const instance = new MyClass();
// Instance method calls are being affected unexpectedly
const result = instance.instanceMethod();
```

### Expected behavior

Instance methods (non-static methods that aren't constructors) should be treated differently from static methods and static blocks during the deoptimization process. Currently, it seems like the logic for determining which class members should be deoptimized is inverted or incorrect.

The deoptimization should skip:
- Static methods/properties
- Constructor methods
- Static blocks

But should apply to regular instance methods.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
