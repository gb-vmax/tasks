# Bug Report

### Describe the bug

I'm experiencing an issue where JavaScript keywords are not being recognized correctly in MDX files. It seems like reserved words (like `if`, `for`, `while`, `function`, etc.) are being treated as regular identifiers instead of keywords.

### Reproduction

When parsing MDX content that contains JavaScript keywords, they're incorrectly tokenized:

```js
// In an MDX file or when parsing MDX content
const Component = () => {
  if (condition) {
    return <div>Hello</div>
  }
}
```

The `if` keyword and other JavaScript reserved words are not being recognized as keywords during the parsing phase. This affects syntax highlighting and potentially code execution in MDX contexts.

### Expected behavior

JavaScript keywords should be properly identified and tokenized as keyword tokens, not as regular name/identifier tokens. The parser should recognize reserved words like `if`, `for`, `while`, `function`, `const`, `let`, `var`, etc. and handle them appropriately.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
