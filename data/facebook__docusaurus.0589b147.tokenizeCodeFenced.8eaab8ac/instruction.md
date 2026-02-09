# Bug Report

### Describe the bug

I'm encountering issues with fenced code blocks in MDX files. It seems like the closing fence detection is not working correctly, causing code blocks to not close properly or close unexpectedly.

### Reproduction

```mdx
\`\`\`js
const example = 'test';
\`\`\`
```

When parsing the above code block, the fence doesn't close as expected. Sometimes it requires extra backticks or behaves inconsistently.

Also seeing issues with indented content inside code blocks - the indentation handling seems off and content is being stripped or processed incorrectly.

### Expected behavior

Fenced code blocks should:
1. Close properly when the closing fence has the same number of backticks as the opening fence
2. Handle indentation within the code block correctly without stripping necessary whitespace

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
