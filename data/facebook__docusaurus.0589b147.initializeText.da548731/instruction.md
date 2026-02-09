# Bug Report

### Describe the bug

I'm encountering an issue where markdown parsing seems to hang or produce incorrect output when processing certain text content. The parser appears to enter an infinite loop or get stuck when handling specific character sequences.

### Reproduction

```js
// Example markdown content that triggers the issue
const markdown = `Some text with special characters...`;

// Parser gets stuck or produces unexpected output
const result = remark.parse(markdown);
```

The issue seems to occur specifically when the parser encounters null characters or reaches end-of-file conditions in certain text contexts. The behavior is inconsistent and sometimes causes the parser to not terminate properly.

### Expected behavior

The markdown parser should correctly handle all text content including edge cases with null characters and EOF conditions, and should always terminate properly without hanging.

### Additional context

This appears to be related to how the text tokenizer handles break conditions. The parser seems to be processing characters in an unexpected order or missing certain exit conditions when dealing with end-of-content scenarios.

---
Repository: /testbed
