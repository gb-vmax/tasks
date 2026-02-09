# Bug Report

### Describe the bug

I'm encountering an issue with class parsing where static methods and properties are being assigned to the wrong scope. It seems like static class members are being treated as instance members and vice versa.

### Reproduction

```js
class MyClass {
  static staticMethod() {
    return 'static';
  }
  
  instanceMethod() {
    return 'instance';
  }
}
```

When this code is processed, the scoping for static vs instance members appears to be reversed. Static methods are being placed in the instance scope and instance methods in the static scope.

### Expected behavior

Static class members should be assigned to the static/class scope, while instance members should be assigned to the instance scope. The current behavior has them swapped.

### Additional context

This is affecting class analysis and potentially tree-shaking behavior for classes with static members. The issue appears to be in how class body definitions are being parsed and assigned to their respective scopes.

---
Repository: /testbed
