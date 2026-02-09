# Bug Report

### Describe the bug

I'm encountering an issue where variable references at the exact same position as their declaration are being incorrectly flagged as Temporal Dead Zone (TDZ) violations. This seems to affect variables declared with `let` or `const` when the reference position matches the declaration position exactly.

### Reproduction

```js
// Example case where this might occur
const x = x; // Self-referencing at declaration
```

Or in more complex scenarios:

```js
let value = someFunction();

function someFunction() {
  return value; // Reference at same position as declaration in AST
}
```

The bundler is treating these cases as TDZ access when they shouldn't be, particularly when the reference position equals the declaration start position rather than being strictly before it.

### Expected behavior

Variable references that occur at the same position as their declaration (or after) should not be flagged as TDZ violations. Only references that occur strictly *before* the declaration should trigger TDZ warnings/errors.

### Additional context

This appears to be related to how the AST position comparison is being performed when checking for TDZ violations. The issue seems to affect the tree-shaking behavior and may cause incorrect warnings or bundling errors.

---
Repository: /testbed
