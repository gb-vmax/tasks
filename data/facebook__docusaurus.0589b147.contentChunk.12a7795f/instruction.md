# Bug Report

### Describe the bug
When parsing fenced code blocks in MDX, the tokenizer is consuming characters incorrectly, causing it to exit the content chunk processing prematurely. This results in malformed parsing of code block content.

### Reproduction
```mdx
```js
const example = 'test';
console.log(example);
```
```

When this code block is parsed, the content tokenization doesn't flow correctly through the state machine. The parser appears to be breaking out of the content chunk loop too early instead of continuing to process characters sequentially.

### Expected behavior
The tokenizer should:
1. Continue consuming characters in the content chunk until it hits a line ending or null
2. Only exit the "codeFlowValue" state when appropriate
3. Properly transition between states in the parsing state machine

The current behavior causes the parser to skip proper content processing and jump states incorrectly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Parser component: tokenizeCodeFenced (codeFlowValue state)

---
Repository: /testbed
