# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in MDX where the closing fence is not being recognized properly. When I have a code block with backticks, the parser seems to be treating the content incorrectly and the code block doesn't close as expected.

### Reproduction

```mdx
# Test Document

```js
function test() {
  return true;
}
```

More content here
```

The parser doesn't seem to properly recognize when the fenced code block ends. The closing fence (the three backticks after the code) should close the block, but it's not working correctly.

### Expected behavior

The fenced code block should be properly closed when encountering a closing fence with the same number (or more) backticks as the opening fence. The content after the closing fence should be parsed as regular markdown content, not as part of the code block.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
