# Bug Report

### Describe the bug

When using classes with methods or properties, the class body inclusion logic appears to be broken. Class definitions are not being properly included in the bundle when `includeChildrenRecursively` is falsy, causing methods and properties to be missing from the output.

### Reproduction

```js
class MyClass {
  constructor() {
    this.value = 42;
  }
  
  myMethod() {
    return this.value;
  }
}

const instance = new MyClass();
console.log(instance.myMethod());
```

When bundling this code, the class body (methods/properties) may not be included correctly in the output, leading to runtime errors or missing functionality.

### Expected behavior

All class methods and properties should be included in the bundle regardless of the inclusion context. The class should work as expected in the bundled output.

### Additional context

This seems to affect class definitions where the body contains methods or properties that need to be traversed and included. The issue appears to be related to how the class body handles recursive inclusion of its child nodes.

---
Repository: /testbed
