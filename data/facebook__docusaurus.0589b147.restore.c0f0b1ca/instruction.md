# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the tokenizer's restore functionality doesn't properly reset the events array. When the parser backtracks during tokenization, events from the previous attempt are still present in the context, leading to duplicate or incorrect parsing results.

### Reproduction

```js
// Parse MDX content that requires backtracking
const mdxContent = `
# Heading

Some content with **bold** text
`;

const result = compile(mdxContent);
// The parsed AST contains duplicate events or incorrect structure
```

This seems to happen when the parser needs to restore state after attempting to parse a construct that ultimately fails. The events array should be cleared back to the starting point, but instead it appears to retain events from the failed parse attempt.

### Expected behavior

When the tokenizer restores to a previous state, the events array should be properly reset to match the state at that point in time. Any events added during the failed parse attempt should be removed.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
