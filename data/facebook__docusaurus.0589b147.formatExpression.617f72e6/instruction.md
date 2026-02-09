# Bug Report

### Describe the bug

I'm encountering an issue where expressions are being wrapped in unnecessary parentheses in the generated output. It looks like the logic for determining when parentheses are needed might be inverted.

### Reproduction

When using MDX with certain JavaScript expressions, the output includes extra parentheses around expressions that don't need them, while expressions that should be parenthesized are missing them.

For example, expressions that have higher precedence and don't require grouping are still being wrapped, making the generated code harder to read and potentially affecting behavior in edge cases.

### Expected behavior

Parentheses should only be added around expressions when they're actually needed for correct precedence or to avoid ambiguity. Expressions that don't need parenthesization should be rendered without the extra wrapping.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
