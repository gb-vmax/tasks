# Bug Report

### Describe the bug

I'm encountering an issue where JavaScript keywords are not being recognized correctly in MDX files. When using reserved keywords like `if`, `else`, `return`, `function`, etc., they are being treated as regular identifiers instead of keywords.

This appears to be affecting syntax highlighting and potentially parsing behavior in MDX documents.

### Reproduction

```js
// In an MDX file, keywords are not being recognized
const test = function() {
  if (true) {
    return false;
  }
}
```

When the above code is parsed, keywords like `function`, `if`, and `return` are being tokenized as regular names instead of their proper keyword types.

### Expected behavior

JavaScript keywords should be recognized and tokenized with the correct type (e.g., `keyword` type) rather than being treated as generic identifiers. This is important for proper syntax highlighting and code parsing.

### System Info
- Package: @mdx-js/mdx@3.0.0
- The issue seems to be in the tokenizer/lexer logic

---
Repository: /testbed
