# Bug Report

### Describe the bug

I'm encountering an issue with class expressions assigned to variables when the class references the variable name itself. It seems like the name mangling/forbidding logic is inverted - names are being forbidden in the wrong cases.

### Reproduction

```js
// Case 1: Class expression assigned to variable
const MyClass = class {
  static getInstance() {
    return new MyClass();
  }
};

// Case 2: Using declaration with class expression
using resource = class Resource {
  [Symbol.dispose]() {
    console.log('disposed');
  }
};
```

When bundling code like this, the variable names are being incorrectly handled. In the first case, when the class references its own variable name (like `MyClass` inside the static method), the name mangling behaves unexpectedly. 

### Expected behavior

Variable names should be properly preserved/forbidden when:
- A class expression is assigned to a variable
- The class body references the variable name
- The variable is not the same as the one being accessed

The current behavior seems to have the logic backwards - it's forbidding names when the variables match instead of when they don't match.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
