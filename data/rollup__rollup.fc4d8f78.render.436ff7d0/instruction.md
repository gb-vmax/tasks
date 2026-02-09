# Bug Report

### Describe the bug

Class expressions are being wrapped in parentheses when they shouldn't be, and not wrapped when they should be. This is causing issues with the generated output code.

### Reproduction

When a class expression is used as a standalone expression statement, it should be wrapped in parentheses to make it valid JavaScript. However, the current behavior seems inverted - parentheses are added in cases where they're not needed, and omitted where they are required.

For example:

```js
// This should be wrapped in parens when rendered as expression statement
class MyClass {
  constructor() {}
}

// But currently getting wrapped when it's NOT an expression statement
// and NOT wrapped when it IS an expression statement
```

This results in invalid JavaScript output in certain contexts.

### Expected behavior

- Class expressions that are expression statements should be wrapped in `()`
- Class expressions in other contexts should not have extra parentheses added

The wrapping logic appears to be backwards from what it should be.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
