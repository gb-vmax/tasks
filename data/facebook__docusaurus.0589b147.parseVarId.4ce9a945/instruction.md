# Bug Report

### Describe the bug

I'm encountering an issue with variable declarations in MDX files. When parsing variable declarations (like `const`, `let`, or `var`), the binding scope seems to be incorrectly assigned. Variables declared with `var` are being treated with lexical scope semantics, and lexical declarations (`const`/`let`) are being treated with `var` scope semantics.

### Reproduction

```js
// In an MDX file
var x = 1;
let y = 2;
const z = 3;

// The parser incorrectly handles the binding scope for these declarations
// var should use BIND_VAR scope
// let/const should use BIND_LEXICAL scope
```

### Expected behavior

- `var` declarations should be assigned `BIND_VAR` scope
- `let` and `const` declarations should be assigned `BIND_LEXICAL` scope

The parser should correctly distinguish between var-scoped and lexically-scoped variable declarations.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
