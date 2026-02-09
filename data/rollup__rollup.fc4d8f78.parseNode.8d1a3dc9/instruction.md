# Bug Report

### Describe the bug

I'm experiencing an issue with class body parsing where class members seem to be getting skipped or incorrectly processed. When defining a class with multiple properties/methods, the first member appears to be missing or undefined in the output.

### Reproduction

```js
class MyClass {
  firstProperty = 1;
  secondProperty = 2;
  thirdProperty = 3;
}
```

When this class is processed, `firstProperty` is not being included properly in the parsed output. It seems like the first element in the class body is being skipped entirely.

### Expected behavior

All class members should be parsed and included in the output, including the first property/method defined in the class body.

### Additional context

This appears to affect any class with multiple members - the first member is consistently missing from the parsed result. Static and instance members both seem to be affected.

---
Repository: /testbed
