# Bug Report

### Describe the bug

I'm experiencing an issue with class expressions in my code where they're being wrapped in parentheses when they shouldn't be. It seems like the bundler is adding extra parentheses around class expressions in contexts where they're not needed.

### Reproduction

```js
// Input code
const MyClass = class {
  constructor() {
    this.value = 42;
  }
};

// After bundling, the class expression gets wrapped incorrectly
const MyClass = (class {
  constructor() {
    this.value = 42;
  }
});
```

The parentheses are being added in places where the class expression is already in a valid expression context (like variable assignments), but they're missing when the class expression is used as a statement.

### Expected behavior

Class expressions should only be wrapped in parentheses when they appear as expression statements (to distinguish them from class declarations). In other contexts like assignments or as function arguments, they shouldn't have extra wrapping.

For example:
- `const x = class {}` - should NOT have parentheses
- `class {}` as a standalone statement - SHOULD have parentheses to make it `(class {})`

### Additional context

This seems to be affecting the output bundle size and readability. The extra parentheses aren't causing runtime errors, but they're unnecessary and the wrapping logic appears to be inverted.

---
Repository: /testbed
