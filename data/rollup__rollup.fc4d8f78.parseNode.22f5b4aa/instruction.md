# Bug Report

### Describe the bug

I'm encountering an issue with class parsing where class members seem to be getting skipped or incorrectly ordered. When I define a class with multiple properties and methods, the first member appears to be missing or undefined at runtime.

### Reproduction

```js
class MyClass {
  firstProperty = 'hello';
  secondProperty = 'world';
  
  myMethod() {
    return this.firstProperty;
  }
}

const instance = new MyClass();
console.log(instance.firstProperty); // undefined or missing
console.log(instance.secondProperty); // 'world'
```

The first property in the class body doesn't seem to be initialized properly. All subsequent properties and methods work as expected.

### Expected behavior

All class members should be properly parsed and accessible, including the first one defined in the class body.

### Additional context

This seems to affect both static and instance members. The issue only appears with the first member - everything else in the class works fine.

---
Repository: /testbed
