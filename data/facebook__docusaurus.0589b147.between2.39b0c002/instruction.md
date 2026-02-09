# Bug Report

### Describe the bug

I'm encountering an issue with inline code (backticks) parsing in markdown. When using backticks in text, the code segments are not being recognized correctly. It seems like the parser is having trouble identifying where inline code blocks start and end.

### Reproduction

```js
// Example markdown content that fails to parse correctly:
const markdown = `This is \`inline code\` in text`;

// The inline code block is not being detected properly
// The backticks appear to be treated incorrectly
```

### Expected behavior

Inline code wrapped in backticks should be properly tokenized and parsed. The content between matching backticks should be treated as code text.

For example:
- Input: `` `code` ``
- Expected: Should recognize this as an inline code block
- Actual: Not parsing correctly

### Additional context

This appears to affect basic inline code formatting. The issue seems related to how the tokenizer handles the backtick character (code 96) when determining code text sequences.

---
Repository: /testbed
