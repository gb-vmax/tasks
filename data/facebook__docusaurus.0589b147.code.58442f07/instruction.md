# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code block rendering in markdown. When I have code blocks that contain backticks in the content, the output is completely broken - either the code block isn't rendered at all or the content is missing.

### Reproduction

```js
const markdown = `
\`\`\`js
const str = \`template string\`;
console.log(str);
\`\`\`
`;

// Process this markdown
// Expected: Code block with 4+ backticks to properly escape the inner backticks
// Actual: Code block uses only 3 backticks, breaking the output
```

When the code content contains backticks (like template literals in JavaScript), the renderer should use more backticks for the fence to properly escape them. Currently it seems to be doing the opposite - using fewer backticks when it should be using more.

### Expected behavior

The code block should be properly fenced with enough backticks to escape any backticks in the content. For example, if the content has 3 consecutive backticks, the fence should use at least 4 backticks.

### Additional context

This seems to have broken recently. The logic for determining the fence sequence length appears to be inverted somehow.

---
Repository: /testbed
