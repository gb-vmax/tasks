# Bug Report

### Describe the bug

I'm experiencing an issue with parsing optional chaining syntax in MDX files. When using optional chaining with template literals (backticks), the parser seems to be incorrectly handling the expression, leading to unexpected parsing behavior.

### Reproduction

```js
const obj = {
  method: () => 'test'
}

// This causes parsing issues
const result = obj?.method?.`template ${string}`
```

When trying to parse MDX content that includes optional chaining followed by template literals, the parser doesn't handle it correctly. The expression should be parsed as separate operations, but instead it seems to be treating them incorrectly.

### Expected behavior

The parser should correctly handle optional chaining syntax when followed by template literals or other valid JavaScript expressions. The optional chaining operator should work as expected without interfering with subsequent operations.

### Additional context

This seems to affect the remark-mdx parser specifically. The issue appears when combining optional chaining (`?.`) with template literals in MDX content.

---
Repository: /testbed
