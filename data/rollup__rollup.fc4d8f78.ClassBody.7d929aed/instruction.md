# Bug Report

### Describe the bug

I'm experiencing issues with class definitions where the first class member is being skipped/ignored, and static vs instance members seem to be getting their scopes mixed up.

### Reproduction

```js
class MyClass {
  firstMethod() {
    return 'first';
  }
  
  secondMethod() {
    return 'second';
  }
  
  static staticMethod() {
    return 'static';
  }
}
```

When I try to use this class:
- The `firstMethod` is not available/accessible
- Static methods seem to be treated as instance methods (or vice versa)
- Only methods after the first one work correctly

### Expected behavior

All class members should be properly parsed and accessible. The first method in the class body should work the same as subsequent methods. Static methods should have access to the static scope, and instance methods should have access to the instance scope.

### Additional context

This seems to affect any class with multiple members. Single-member classes might work by accident, but anything with 2+ members has the first one missing or incorrectly scoped.

---
Repository: /testbed
