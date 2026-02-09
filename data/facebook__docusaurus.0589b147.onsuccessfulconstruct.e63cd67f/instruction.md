# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the tokenizer appears to be using incorrect position information when processing constructs. After some investigation, it seems like the tokenizer is referencing the wrong position property when adding results for successful constructs.

### Reproduction

When parsing MDX content with nested constructs, the position tracking gets out of sync. This causes the parser to produce incorrect results or fail to properly tokenize certain patterns.

```js
// Example MDX content that triggers the issue
const mdxContent = `
# Heading

Some text with **bold** and _italic_.

- List item 1
- List item 2
`;

// Parse the content
const result = await compile(mdxContent);
// Position information is incorrect for nested elements
```

### Expected behavior

The tokenizer should correctly track positions using the appropriate boundary (either `from` or `to`) when constructs are successfully processed. The current behavior seems to be using the wrong position reference, which leads to incorrect parsing results.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This appears to be a regression as the parsing was working correctly in previous versions. The issue manifests particularly with nested or complex MDX structures where position tracking is critical.

---
Repository: /testbed
