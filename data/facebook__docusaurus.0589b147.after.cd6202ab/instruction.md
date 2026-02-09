# Bug Report

### Describe the bug

I'm experiencing an issue with parsing fenced code blocks in markdown. After parsing completes, the parser seems to be returning the wrong value, which causes downstream processing to fail or behave unexpectedly.

### Reproduction

```js
const processor = remark();
const ast = processor.parse('```js\nconsole.log("test");\n```');
// Processing fails or returns unexpected results
```

When parsing markdown with fenced code blocks, the tokenizer appears to be returning an incorrect value after processing the closing fence. This breaks the parsing flow and can cause the entire document to be parsed incorrectly.

### Expected behavior

Fenced code blocks should be parsed correctly and the tokenizer should return the appropriate continuation value to allow the parser to continue processing the rest of the document normally.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
