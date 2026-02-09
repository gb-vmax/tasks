# Bug Report

### Describe the bug

I'm encountering an issue with class declarations where variable names are being incorrectly forbidden. It seems like the name collision detection logic is working backwards - variables that should have their names forbidden are not being affected, while unrelated variables are being incorrectly restricted.

### Reproduction

```js
class MyClass {
  constructor() {
    // When there's a variable with the same name as the class
    // in the outer scope, it's not being handled correctly
  }
}

const MyClass = 'something'; // This should cause a name conflict
```

The bundler is not properly preventing name collisions between class declarations and variables in outer scopes that are accessed from within the class.

### Expected behavior

When a class declaration has the same name as a variable that's accessed from outside the class scope, the bundler should properly forbid the use of that name to prevent conflicts during code generation.

### Additional context

This appears to be related to how the AST handles class declarations and their interaction with variables in outer scopes. The name forbidding mechanism seems to be applied to the wrong set of variables.

---
Repository: /testbed
