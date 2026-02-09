# Bug Report

### Describe the bug

I'm experiencing an issue with code fence rendering in markdown. When I have a code block that contains backticks in the content, the output doesn't properly escape them and the fence markers are not using the correct number of characters.

### Reproduction

```js
const markdown = `
\`\`\`js
const code = \`template string\`;
\`\`\`
`;

// Process this markdown
const result = processMarkdown(markdown);
```

When the code block content has backticks (like template strings in JavaScript), the fence markers should use enough backticks to properly delimit the block, but they don't seem to be calculating the right length anymore.

Also noticed that code blocks without trailing newlines in the raw content are getting an extra newline added when they shouldn't.

### Expected behavior

- Code fences should use at least one more backtick than the longest streak found in the content to properly escape it
- Raw content should only get a trailing newline added if it already ends with one

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
