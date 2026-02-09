# Bug Report

### Describe the bug

I'm experiencing an issue with expression formatting in MDX where parentheses are being placed incorrectly around expressions. It appears that when an expression requires parentheses for proper precedence, the opening and closing parentheses are not being written in the correct order relative to the expression itself.

### Reproduction

When processing MDX content with expressions that need parenthesization (e.g., complex binary operations, conditional expressions), the generated output has malformed syntax with parentheses in the wrong positions.

For example, expressions that should be wrapped like `(expression)` are instead being generated with incorrect parenthesis placement, causing the output to be syntactically invalid.

### Expected behavior

Expressions that require parentheses should have the opening parenthesis written first, followed by the expression content, and then the closing parenthesis. The current behavior seems to be writing parts of the expression before the opening parenthesis or the closing parenthesis in the wrong branch of the conditional logic.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
