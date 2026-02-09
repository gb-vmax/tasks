# Bug Report

### Describe the bug

Class expressions are getting wrapped in parentheses when they shouldn't be, causing incorrect code generation. The wrapping behavior seems to be inverted - parentheses are added in contexts where they're not needed and omitted where they should be present.

### Reproduction

```js
// When a class expression is used as an expression statement
// it should be wrapped in parentheses, but currently it's not

class MyClass {}

// In other contexts (e.g., assigned to a variable, passed as argument)
// parentheses shouldn't be added, but they are being added incorrectly

const MyClass = class {};
```

The generated output has the wrapping logic backwards - class expressions that need parentheses don't get them, and those that don't need them are getting wrapped.

### Expected behavior

- Class expressions used as standalone expression statements should be wrapped in parentheses
- Class expressions in other contexts (assignments, arguments, etc.) should not have extra parentheses added

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
