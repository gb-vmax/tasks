# Bug Report

### Describe the bug

I'm experiencing an issue where the first method/property in a class definition is being skipped during bundling. When I define a class with multiple methods, the first one doesn't appear in the output bundle, causing runtime errors when trying to call it.

### Reproduction

```js
class MyClass {
  firstMethod() {
    return 'first';
  }
  
  secondMethod() {
    return 'second';
  }
  
  thirdMethod() {
    return 'third';
  }
}

const instance = new MyClass();
console.log(instance.firstMethod()); // Error: firstMethod is not a function
console.log(instance.secondMethod()); // Works fine
console.log(instance.thirdMethod()); // Works fine
```

The first method in the class body seems to be completely missing from the bundled output. All subsequent methods work as expected.

### Expected behavior

All class methods should be included in the bundle, including the first one. The `firstMethod()` call should return `'first'` without throwing an error.

### Additional context

This appears to affect any class definition regardless of whether it's a regular method, getter, setter, or static method - whatever is defined first in the class body gets dropped.

---
Repository: /testbed
