# Bug Report

### Describe the bug

Member expressions with optional chaining are generating incorrect code. When using optional chaining with computed property access (e.g., `obj?.[prop]`), the output is malformed and produces invalid JavaScript syntax.

### Reproduction

```js
// Input code with optional chaining and computed property
const result = obj?.[key]

// Expected output:
// obj?.[key]

// Actual output (malformed):
// obj?.key (missing brackets)
```

Also seeing issues with parentheses placement around member expressions. In some cases, parentheses that should wrap the object are being omitted, while in other cases they're being added when they shouldn't be.

### Expected behavior

- Optional chaining with computed properties should preserve the bracket notation: `obj?.[prop]`
- Parentheses should be correctly placed around objects that need them based on precedence rules
- Generated code should be valid JavaScript that can be executed

### Additional context

This is affecting code generation for member expressions in the MDX compiler. The generated output is syntactically invalid and causes runtime errors when trying to execute the compiled code.

---
Repository: /testbed
