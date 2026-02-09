# Bug Report

### Describe the bug

I'm encountering an issue where JavaScript keywords are not being recognized correctly by the parser. When I use reserved keywords in my MDX files, they're being treated as regular identifiers instead of keywords.

### Reproduction

```js
// In an MDX file
const myVar = function() {
  return true
}

// Keywords like 'function', 'return', 'const' etc. are not being parsed correctly
// They're treated as regular names instead of keywords
```

The parser seems to be checking keywords against the wrong token value, causing it to fail to identify reserved words properly.

### Expected behavior

Reserved JavaScript keywords should be correctly identified and tokenized as keyword types, not as generic name tokens. For example, `function`, `return`, `const`, `let`, `if`, `else`, etc. should all be recognized as their respective keyword token types.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
