# Bug Report

### Describe the bug

When using `this` in class instance methods, the scope resolution seems to be incorrect. The `this` variable in the class body scope and instance scope appear to have their assignments swapped, causing issues with proper context binding.

### Reproduction

```js
class MyClass {
  constructor() {
    this.value = 42;
  }
  
  method() {
    // this should refer to the instance
    return this.value;
  }
  
  static staticMethod() {
    // this should refer to the class itself
    return this;
  }
}

const instance = new MyClass();
instance.method(); // Expected to work correctly but context is wrong
```

### Expected behavior

- Instance methods should have `this` bound to the instance scope
- Static methods and class body should have `this` bound to the class scope
- The scope chain should properly distinguish between class-level and instance-level `this` references

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
