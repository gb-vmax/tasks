# Bug Report

### Describe the bug

When using class declarations with inheritance, the class name is not being preserved correctly in the output. The generated code appears to be using the wrong variable names for class references within the class body.

### Reproduction

```js
class MyClass extends BaseClass {
  constructor() {
    super();
    this.name = MyClass.name; // Should reference the class itself
  }
  
  static create() {
    return new MyClass();
  }
}
```

After bundling, the class references inside the class body are being renamed incorrectly, causing the code to break or behave unexpectedly.

### Expected behavior

The class name should be preserved when referenced within its own body (constructor, methods, static methods, etc.). Internal references to `MyClass` should remain as `MyClass` or be consistently renamed throughout the class body.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
