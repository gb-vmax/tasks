# Bug Report

### Describe the bug

I'm encountering an issue where JavaScript keywords are not being recognized properly in MDX files. It seems like all keywords (like `if`, `else`, `function`, `return`, etc.) are being treated as regular identifiers instead of their proper token types.

### Reproduction

When parsing MDX content that contains JavaScript keywords, they're all being tokenized as `name` tokens instead of their specific keyword types. For example:

```js
// In an MDX file
function myComponent() {
  if (true) {
    return <div>Hello</div>
  }
}
```

All of `function`, `if`, and `return` are being treated as generic names rather than keywords, which breaks syntax highlighting and potentially other downstream processing.

### Expected behavior

Keywords should be properly identified and tokenized with their correct keyword type (e.g., `function` should be tokenized as a function keyword, `if` as a conditional keyword, etc.), not as generic name tokens.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems to have started happening recently. Any help would be appreciated!

---
Repository: /testbed
