# Bug Report

### Describe the bug

Class declarations are being incorrectly wrapped with variable assignments when the class name matches the rendered variable name. This causes the generated code to have unexpected `let` assignments around class declarations that should remain as standard class declarations.

### Reproduction

```js
// Input code
class MyClass {
  constructor() {
    this.value = 42;
  }
}

// Expected output: class declaration remains unchanged
class MyClass {
  constructor() {
    this.value = 42;
  }
}

// Actual output: class is wrapped with variable assignment
let MyClass = class MyClass {
  constructor() {
    this.value = 42;
  }
};
```

### Expected behavior

When a class declaration's name matches its rendered variable name (the common case), the class should be rendered as a normal class declaration without being converted to a class expression assigned to a variable. The variable assignment wrapper should only be applied when the rendered variable name differs from the original class name.

### Additional context

This appears to affect all class declarations where renaming is not required, resulting in unnecessary code transformations that change the semantics of the code (class declarations are hoisted, but variable assignments are not).

---
Repository: /testbed
