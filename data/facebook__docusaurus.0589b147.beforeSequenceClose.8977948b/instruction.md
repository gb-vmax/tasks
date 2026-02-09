# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in markdown parsing. When I try to use code fences (triple backticks), the closing fence sequence isn't being recognized properly, which causes the parser to treat everything after the opening fence as code content, even when there's a proper closing fence.

### Reproduction

```markdown
```js
function test() {
  return 'hello';
}
```
```

When parsing the above markdown, the closing fence (```) is not being detected correctly, and the parser continues treating subsequent content as part of the code block instead of closing it properly.

### Expected behavior

The parser should correctly identify the closing fence sequence and close the code block. Any content after the closing fence should be parsed as regular markdown content, not as part of the code block.

### Additional context

This seems to affect all fenced code blocks regardless of the language identifier used. The opening fence is detected fine, but the closing sequence doesn't trigger the proper state transition in the tokenizer.

---
Repository: /testbed
