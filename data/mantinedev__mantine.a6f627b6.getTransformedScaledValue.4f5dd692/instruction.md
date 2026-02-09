# Bug Report

### Describe the bug

I'm experiencing an issue with CSS `calc()` values not being parsed correctly. When I use `calc()` expressions with multiplication, the function seems to be extracting the wrong part of the calculation.

### Reproduction

```js
// When using calc with multiplication like:
const value = 'calc(100px * 2)';

// The parsed result is incorrect - it appears to be taking 
// the second operand instead of the first one
```

This is affecting any component that uses calc expressions with the `*` operator. The scaling/transformation logic seems to be broken.

### Expected behavior

When parsing a `calc()` expression like `calc(100px * 2)`, it should extract `100px` (the first operand), not `2` (the second operand).

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
