# Bug Report

### Describe the bug

I'm experiencing an issue with parsing fenced code blocks in markdown. When processing markdown with multiple consecutive fenced code blocks, the content seems to be getting duplicated or merged incorrectly.

### Reproduction

```js
const markdown = `
\`\`\`js
const x = 1;
\`\`\`

\`\`\`js
const y = 2;
\`\`\`
`;

// Parse the markdown
const result = remark().parse(markdown);

// The second code block contains content from both blocks
// or the blocks are not properly separated
```

### Expected behavior

Each fenced code block should be parsed independently with its own content. The second code block should only contain `const y = 2;` and not include content from the first block.

### Additional context

This seems to affect consecutive code blocks specifically. Single code blocks work fine, but when you have multiple code blocks one after another, the parsing gets confused.

---
Repository: /testbed
