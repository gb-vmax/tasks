# Bug Report

### Describe the bug

I'm experiencing an issue with code fence rendering in markdown. When I have code blocks that contain backticks in the content, the output is malformed and doesn't properly escape the fence markers.

### Reproduction

```js
const markdown = `
\`\`\`js
const code = \`template string\`;
console.log(\`\`\`multiple backticks\`\`\`);
\`\`\`
`;

// Parse and stringify the markdown
const result = remark().stringify(remark().parse(markdown));
console.log(result);
```

The output has incorrect fence markers - it uses 3 backticks even when the content contains sequences of 3 or more backticks, which breaks the code block.

### Expected behavior

The fence markers should use enough backticks to properly wrap the content. If the code contains 3 backticks, the fence should use 4 or more backticks to avoid conflicts. The closing fence should also be on its own line.

For example, if the content has ` ``` ` inside, the output should use `````  (4+ backticks) as the fence markers.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
