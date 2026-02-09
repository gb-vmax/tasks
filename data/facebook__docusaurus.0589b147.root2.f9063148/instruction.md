# Bug Report

### Describe the bug

I'm experiencing an issue with JSX expression containers in MDX. When I have literal expressions with whitespace content, they're not being handled correctly. It seems like the code is trying to access the wrong property on the expression object.

### Reproduction

```jsx
<div>
  {" "}
  <span>content</span>
  {"\n"}
</div>
```

When processing JSX like the above, where there are literal string expressions containing only whitespace, the parser appears to be looking at the wrong data field. Instead of checking the expression's value, it's checking something else which causes the whitespace detection to fail.

### Expected behavior

Whitespace-only literal expressions in JSX should be properly detected and handled. The parser should correctly identify when a `JSXExpressionContainer` contains a `Literal` expression with whitespace content and process it accordingly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This might be related to how literal expression values are accessed in the AST structure. The whitespace cleaning logic seems to be breaking down for these specific cases.

---
Repository: /testbed
