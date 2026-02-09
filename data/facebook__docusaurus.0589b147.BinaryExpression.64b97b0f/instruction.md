# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX code generator where `in` operator expressions are being wrapped in parentheses when they shouldn't be, and other binary expressions are missing parentheses when they should have them.

### Reproduction

When using the `in` operator in MDX expressions, the generated code incorrectly adds parentheses around the entire expression:

```js
// Input MDX expression
{key in object}

// Generated output (incorrect)
(key in object)

// Expected output
key in object
```

Similarly, other binary expressions that should be wrapped in parentheses are not being wrapped correctly.

### Expected behavior

- The `in` operator should NOT be wrapped in parentheses
- Other binary expressions should be wrapped in parentheses where appropriate
- The left and right operands should maintain correct precedence handling

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken after a recent update. The parentheses logic appears to be inverted for the `in` operator.

---
Repository: /testbed
