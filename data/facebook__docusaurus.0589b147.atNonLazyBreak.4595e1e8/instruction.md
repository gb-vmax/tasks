# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code block parsing in remark. When processing markdown with fenced code blocks, the parser seems to be handling line breaks incorrectly, causing the content to be parsed in the wrong order or not recognized properly.

### Reproduction

```markdown
```js
function test() {
  return true;
}
```
```

When this markdown is parsed, the code block content is not being properly recognized. The closing fence seems to be evaluated at the wrong time during tokenization.

### Expected behavior

The parser should correctly identify the fenced code block boundaries and parse the content between the opening and closing fences as code content. The line breaks within the code block should be handled properly without prematurely attempting to close the block.

### Additional context

This appears to be related to how the tokenizer handles non-lazy line breaks within fenced code blocks. The sequence of checking for closing fences versus continuing with content parsing seems off.

---
Repository: /testbed
