# Bug Report

### Describe the bug

I'm encountering an issue where class expressions assigned to variables are getting incorrectly named in the output. When a class expression is assigned to a variable and the variable name differs from the internal class reference, the class name is being added even when it shouldn't be.

### Reproduction

```js
// Input code
const MyClass = class {};
export { MyClass as RenamedClass };

// Expected output: class expression should remain anonymous
const MyClass = class {};

// Actual output: class name is incorrectly added
const MyClass = class MyClass {};
```

This causes issues when the variable is exported with a different name, as the class gets an unnecessary internal name that doesn't match the export.

### Expected behavior

Class expressions should only receive an internal name when the rendered variable name differs from the original variable name. If they match, the class should remain anonymous as in the original source code.

### Additional context

This seems to be related to variable declarators with class expression initializers. The logic for determining when to add a class name appears to be inverted - it's adding names when it shouldn't and vice versa.

---
Repository: /testbed
