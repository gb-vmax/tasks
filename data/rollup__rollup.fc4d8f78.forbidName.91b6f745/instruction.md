# Bug Report

### Describe the bug

I'm experiencing an issue with export default variable name handling. When trying to use certain identifiers that should be forbidden, the validation doesn't work correctly and allows names that should be rejected.

### Reproduction

```js
// module.js
export default class MyClass {
  // class definition
}

// In another file, when the bundler tries to assign a name
// that conflicts with a reserved identifier, it doesn't
// properly forbid the name
```

The issue seems to be related to how the `forbidName` method handles the original variable reference. When I have an export default declaration, the name validation logic doesn't behave as expected.

### Expected behavior

The bundler should properly forbid conflicting names for export default variables, preventing name collisions with reserved identifiers or other variables in the scope.

### Additional context

This appears to have started happening recently. The logic for checking the original variable seems inverted - it's calling the parent method when it shouldn't and returning early in the wrong cases.

---
Repository: /testbed
