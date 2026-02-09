# Bug Report

### Describe the bug

Class expressions are being wrapped in parentheses incorrectly when they're not part of an expression statement. This causes invalid JavaScript output in certain contexts.

### Reproduction

```js
// When a class expression appears in a context other than an expression statement
// (e.g., as part of a variable declaration, return statement, etc.)
// it's getting wrapped with parentheses in the wrong positions

const MyClass = class {
  constructor() {}
};

// Or in a return statement
function getClass() {
  return class {
    method() {}
  };
}
```

After bundling, the output has malformed parentheses placement that breaks the syntax.

### Expected behavior

Class expressions should only be wrapped in parentheses when they appear as expression statements (to avoid being parsed as class declarations). In all other contexts, they should remain unwrapped or the parentheses should be placed correctly.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
