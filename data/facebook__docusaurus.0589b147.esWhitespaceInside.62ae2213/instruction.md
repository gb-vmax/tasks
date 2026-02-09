# Bug Report

### Describe the bug

I'm experiencing an issue with whitespace handling in JSX expressions within MDX files. When there's whitespace (spaces or unicode whitespace characters) inside JSX tags, the parser seems to be consuming the character before checking what type of whitespace it is, which causes incorrect parsing behavior.

### Reproduction

```jsx
<Component
  prop={  value  }
/>
```

When parsing JSX with whitespace inside the curly braces or between attributes, the whitespace isn't being handled correctly. It looks like the parser is now consuming characters before determining if they're markdown line endings or regular spaces, leading to unexpected token consumption.

### Expected behavior

The parser should properly identify and handle different types of whitespace (markdown spaces, unicode whitespace, line endings) before consuming them. Whitespace inside JSX expressions should be processed correctly without affecting the parsing state.

### System Info
- MDX version: 3.0.0
- Parser: remark-mdx

This seems to have broken after a recent change to the whitespace handling logic in the JSX parser. The order of operations for checking and consuming whitespace appears to be incorrect now.

---
Repository: /testbed
