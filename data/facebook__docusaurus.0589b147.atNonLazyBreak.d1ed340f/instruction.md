# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in markdown parsing. When a code block contains content before the closing fence, the parser seems to be handling the continuation incorrectly. The closing fence detection appears to be executing callbacks in the wrong order.

### Reproduction

```markdown
```js
function test() {
  return true;
}
```
```

When parsing the above fenced code block, the parser doesn't properly process the content lines before attempting to match the closing fence. This affects how the code block content is tokenized.

### Expected behavior

The parser should:
1. First process any content lines within the code block
2. Then attempt to match the closing fence
3. Only proceed to the "after" state once the fence is properly closed

Instead, it seems like the callbacks are being invoked in an unexpected order, causing the content to not be processed correctly before checking for the closing fence.

### System Info
- remark version: 15.0.1
- Parser: micromark-based tokenizer

---
Repository: /testbed
