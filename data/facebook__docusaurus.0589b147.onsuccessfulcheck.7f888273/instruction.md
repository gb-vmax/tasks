# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where certain markdown constructs are causing unexpected behavior. It seems like the tokenizer's check mechanism isn't properly restoring state in some edge cases.

### Reproduction

When processing MDX content with specific nested structures, the parser appears to be calling `restore()` on the wrong object. This leads to inconsistent parsing results.

```js
// Example MDX content that triggers the issue
const mdxContent = `
# Title

Some content with **bold** and _italic_

\`\`\`js
code block
\`\`\`
`;

// Parse the content
const result = await compile(mdxContent);
```

### Expected behavior

The parser should correctly restore tokenizer state after successful checks, ensuring that all markdown constructs are parsed consistently regardless of nesting depth or complexity.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This appears to be related to how the `onsuccessfulcheck` callback handles the info parameter. The restoration logic seems to be inverted or checking the wrong condition.

---
Repository: /testbed
