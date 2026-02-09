# Bug Report

### Describe the bug

I'm experiencing an issue with CSS `calc()` values that include multiplication operations. When using a value like `calc(2 * var(--some-value))`, the library seems to be extracting the wrong part of the expression.

### Reproduction

```js
// Using a calc value with multiplication
const value = 'calc(2 * var(--mantine-spacing-md))';

// The transformed value returns the multiplier instead of the variable
// Expected: 'var(--mantine-spacing-md)'
// Actual: '2'
```

### Expected behavior

When parsing `calc()` expressions with multiplication, the function should extract the CSS variable or unit value (the second operand after the `*`), not the numeric multiplier (the first operand).

For example:
- Input: `calc(2 * var(--spacing))` 
- Should return: `var(--spacing)`
- Currently returns: `2`

### System Info
- @mantine/core version: latest
- Browser: Chrome

---
Repository: /testbed
