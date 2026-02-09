# Bug Report

### Describe the bug

I'm experiencing unexpected behavior with class instantiation and static properties. When creating instances of classes, the constructor seems to be getting called even when it shouldn't be, and static properties/methods are appearing on instances instead of on the class itself.

### Reproduction

```js
class MyClass {
  static staticMethod() {
    return 'static';
  }
  
  constructor() {
    console.log('Constructor called');
  }
  
  instanceMethod() {
    return 'instance';
  }
}

// Static methods are incorrectly appearing as instance properties
const instance = new MyClass();
```

### Expected behavior

- Static methods and properties should only be accessible on the class itself, not on instances
- Constructor should only be called when using `new` keyword
- Instance properties should be separate from static properties

### System Info
- Rollup version: latest
- Node: v18.x

---
Repository: /testbed
