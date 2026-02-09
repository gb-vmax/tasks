# Bug Report

### Describe the bug

I'm encountering an issue with code fence parsing in markdown. When processing fenced code blocks, the parser seems to get stuck in an infinite loop or fails to properly exit line endings within the code block content.

### Reproduction

```js
const markdown = `
\`\`\`js
function test() {
  return true;
}
\`\`\`
`;

// Parser hangs or produces incorrect output when processing this
```

### Expected behavior

The parser should correctly handle line endings within fenced code blocks and properly transition between content states. The code block should be parsed completely without getting stuck.

### Additional context

This appears to affect multi-line code blocks specifically. Single-line code blocks seem to work fine. The issue manifests when the parser encounters line endings while processing the content of a fenced code block.

---
Repository: /testbed
