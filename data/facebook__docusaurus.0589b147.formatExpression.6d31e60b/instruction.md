# Bug Report

### Describe the bug
When using expressions that require parentheses in MDX files, the parentheses are being placed incorrectly in the generated output. The closing parenthesis appears before the expression content instead of wrapping it properly.

### Reproduction
```jsx
// Example MDX content with an expression that needs parentheses
{someCondition ? (
  <Component prop={value} />
) : null}
```

When this gets processed, the parentheses end up in the wrong position in the generated code, causing syntax errors or unexpected behavior.

### Expected behavior
Expressions that need parentheses should have them wrapped correctly around the entire expression: `(expression)` not `expression()`.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
