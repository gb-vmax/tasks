# Bug Report

### Describe the bug

I'm experiencing an issue with inline code parsing in markdown. When trying to parse text with backticks (inline code), the parser seems to be breaking or not returning properly. The code that was working before now appears to hang or fail silently.

### Reproduction

```js
const markdown = 'This is `inline code` in text';
const result = remark().parse(markdown);
// Parser doesn't complete or returns unexpected result
```

Also happens with:
```js
const text = 'Use `console.log()` to debug';
// Parsing this text doesn't work as expected
```

### Expected behavior

The parser should correctly identify and tokenize inline code blocks wrapped in backticks. The AST should contain proper `codeText` nodes for the inline code segments.

### Additional context

This seems to have started happening recently. Regular text without backticks parses fine, but as soon as I include inline code with backticks, something goes wrong with the tokenization process.

---
Repository: /testbed
