# Bug Report

### Describe the bug

I'm encountering an issue with variable declarations where the first declarator in a declaration statement doesn't seem to be properly initialized. When I have multiple variables declared in a single statement, only the subsequent variables (after the first one) are being handled correctly.

### Reproduction

```js
// This declaration doesn't work as expected
const a = 1, b = 2, c = 3;

// The first variable 'a' is not properly declared
// but 'b' and 'c' work fine
```

The problem occurs specifically with the first variable in a multi-variable declaration. Single variable declarations might work, but when you have multiple declarators separated by commas, the first one isn't being processed correctly.

### Expected behavior

All variables in a declaration statement should be properly declared and initialized, regardless of their position. The first declarator should behave the same way as the others.

### Additional context

This seems to affect `const`, `let`, and `var` declarations equally. The issue is particularly noticeable when the first variable is referenced later in the code - it's as if it was never declared at all.

---
Repository: /testbed
