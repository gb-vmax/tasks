# Bug Report

### Describe the bug

I've encountered an issue with class constructor detection when parsing JavaScript classes. It seems like the constructor property is not being set correctly when a class actually has a constructor defined.

### Reproduction

```js
class MyClass {
  constructor(value) {
    this.value = value;
  }
  
  method() {
    return this.value;
  }
}
```

When parsing a class like the one above, the constructor is found during iteration over the class body, but it appears that the constructor reference is being overwritten or reset afterward. This causes issues when trying to access or analyze the constructor later in the compilation process.

### Expected behavior

When a class has a constructor method, the `classConstructor` property should be set to that constructor method and remain set. The constructor should be properly identified and retained for subsequent processing.

### Additional context

This seems to affect any class that has a constructor defined. Classes without constructors work fine (correctly set to `null`), but classes with constructors are not being handled properly.

---
Repository: /testbed
