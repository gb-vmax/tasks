# Bug Report

### Describe the bug

Class expressions are being wrapped with parentheses incorrectly, causing syntax errors in the generated output. It appears that parentheses are being added in the wrong positions or at the wrong times.

### Reproduction

```js
// When a class expression is used in certain contexts
const MyClass = class {
  constructor() {
    this.value = 42;
  }
};

// Or as an IIFE
new class {
  method() {
    return 'test';
  }
}();
```

After bundling, the output has parentheses in unexpected places, leading to invalid JavaScript syntax.

### Expected behavior

Class expressions should only be wrapped with parentheses when they appear as expression statements (to avoid ambiguity with class declarations). In other contexts, they should remain unwrapped.

The generated code should be valid JavaScript that runs without syntax errors.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
