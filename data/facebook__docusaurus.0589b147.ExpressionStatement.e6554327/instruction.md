# Bug Report

### Describe the bug

I'm experiencing an issue with expression statement generation where certain expressions are being wrapped in parentheses when they shouldn't be, or vice versa. This is causing incorrect code output in the generated JavaScript.

### Reproduction

When generating code for expression statements with specific precedence levels, the logic for determining when to add parentheses seems to be inverted or incorrectly checking the condition. This affects expressions where:
- The precedence is less than or equal to 3
- The left side of the expression doesn't start with "O"

```js
// Example scenarios that may be affected:
// - Assignment expressions
// - Binary expressions with certain operators
// - Expressions that should/shouldn't be wrapped based on precedence
```

The generated output either has unnecessary parentheses or is missing required parentheses, which can change the semantics of the code or cause syntax errors.

### Expected behavior

Expression statements should be correctly wrapped in parentheses only when necessary based on their precedence and type, following standard JavaScript grammar rules.

### System Info
- Package: @mdx-js/mdx
- Version: 3.0.0

---
Repository: /testbed
