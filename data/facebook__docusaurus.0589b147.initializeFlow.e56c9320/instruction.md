# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where line endings after flow content are being incorrectly tokenized. When a line ending follows a flow construct (like a code block or other block-level element), it's being marked as `lineEndingBlank` instead of `lineEnding`, which causes problems with subsequent parsing.

### Reproduction

```js
const markdown = `\`\`\`
code block
\`\`\`
next line`;

// Parse the markdown
const result = processor.parse(markdown);

// The line ending after the code block gets the wrong token type
// Expected: "lineEnding"
// Actual: "lineEndingBlank"
```

### Expected behavior

Line endings after flow constructs should be tokenized as `lineEnding` tokens, not `lineEndingBlank` tokens. The `lineEndingBlank` type should only be used for actual blank lines, not for regular line endings that happen to follow block-level content.

This affects the AST structure and can break downstream processing that relies on correct token types.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
