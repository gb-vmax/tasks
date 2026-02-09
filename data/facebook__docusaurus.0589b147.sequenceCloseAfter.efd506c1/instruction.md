# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks not closing properly in MDX. When I have a code fence (using triple backticks), the parser seems to be rejecting valid closing sequences. The code block just continues indefinitely instead of being properly terminated.

### Reproduction

```mdx
```javascript
function test() {
  return true;
}
```

Some text after the code block
```

When parsing this, the closing fence isn't being recognized correctly and the entire rest of the document gets treated as part of the code block.

### Expected behavior

The code fence should close normally when it encounters three backticks on a new line. The parser should recognize the closing fence and exit the code block, allowing the subsequent content to be parsed as regular MDX content.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken recently - code fences were working fine before. Any help would be appreciated!

---
Repository: /testbed
