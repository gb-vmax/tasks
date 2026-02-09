# Bug Report

### Describe the bug

I'm encountering an issue with variable declarations in MDX files. When parsing variable declarations, the parser seems to be incorrectly validating the binding patterns, which causes variables declared with `let` or `const` to be treated incorrectly.

### Reproduction

```jsx
// In an MDX file
const myVar = 'test';
let anotherVar = 'value';

// These declarations are not being parsed correctly
```

The issue appears to affect how the parser determines whether a variable should be bound as `BIND_VAR` or `BIND_LEXICAL`. The validation logic seems to be checking the wrong value when determining the binding type.

### Expected behavior

Variable declarations with `const` and `let` should be properly recognized and bound as lexical bindings (`BIND_LEXICAL`), while `var` declarations should use variable bindings (`BIND_VAR`). The parser should correctly distinguish between these declaration types.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
