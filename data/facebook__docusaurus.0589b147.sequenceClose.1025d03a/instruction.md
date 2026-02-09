# Bug Report

### Describe the bug

I'm experiencing an issue with parsing inline code blocks (backticks) in markdown. When using multiple backticks to create inline code, the parser seems to hang or behave unexpectedly.

### Reproduction

```js
// Try parsing markdown with inline code using backticks
const markdown = `
Some text with \`\`code here\`\` and more text.
`;

// Parser appears to hang or produce unexpected output
```

Specifically, when the markdown contains inline code delimited by double backticks (or more), the tokenizer doesn't seem to properly close the code sequence and process the rest of the content.

### Expected behavior

The parser should correctly tokenize inline code blocks regardless of how many backticks are used to delimit them (as long as opening and closing sequences match). The content should be parsed without hanging or getting stuck in an infinite loop.

### Additional context

This seems to affect the `tokenizeCodeText` function in the micromark tokenizer. The issue appears when processing the closing backtick sequence - it's not returning control properly to continue parsing the rest of the document.

---
Repository: /testbed
