# Bug Report

### Describe the bug

I'm experiencing an issue with text parsing where the parser appears to get stuck in an infinite loop or stops processing text correctly. The markdown processor seems to hang or produce incorrect output when processing certain text patterns.

### Reproduction

```js
const processor = remark();
const text = `Some text content with special characters or line breaks`;
const result = processor.processSync(text);
// Parser hangs or produces unexpected results
```

When processing markdown text, the parser doesn't seem to advance correctly through the content. It looks like it might be stuck re-processing the same character or section repeatedly instead of moving forward through the text.

### Expected behavior

The parser should process the text sequentially, consuming each character and moving to the next state correctly. Text data should be parsed completely without hanging or getting stuck.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
