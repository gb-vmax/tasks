# Bug Report

### Describe the bug

I'm experiencing an issue with code fence rendering in markdown. When I have code blocks that contain backticks or tildes in the content, the output doesn't properly escape them and the fence markers become too short, breaking the markdown structure.

### Reproduction

```js
const markdown = `
\`\`\`
Code with ``` backticks inside
\`\`\`
`;

// The output uses only 3 backticks as fence markers
// This causes the inner backticks to break out of the code block
```

When the code content has sequences of backticks (like ````), the fence markers should use at least one more backtick than the longest sequence found in the content. But it seems like it's using fewer markers instead.

### Expected behavior

The code fence should always use enough markers to properly contain the content. If the content has 3 consecutive backticks, the fence should use at least 4 backticks.

For example:
- Content has `` ` `` → use ```` ``` ````
- Content has ```` ``` ```` → use ````` ```` `````
- Content has ````` ```` ````` → use `````` ````` ``````

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
