# Bug Report

### Describe the bug

I'm experiencing an infinite loop issue when parsing inline code blocks with backticks in MDX content. The parser seems to get stuck and never completes when processing code text sequences.

### Reproduction

```js
const mdx = `
This is some text with \`inline code\` in it.
`;

// Parser hangs indefinitely when processing the backticks
compile(mdx);
```

### Expected behavior

The parser should successfully tokenize the inline code block and complete processing without hanging. The backtick sequences should be properly opened and closed, allowing the parser to continue to the next token.

### Additional context

This appears to happen specifically when the parser encounters backtick characters (code 96). The tokenization process doesn't seem to exit the sequence properly and gets caught in an endless loop.

---
Repository: /testbed
