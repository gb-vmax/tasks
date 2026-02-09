# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where the tokenizer appears to be skipping constructs or not properly iterating through the list of constructs when a construct fails to match. This seems to be causing certain MDX syntax patterns to not be recognized correctly.

### Reproduction

```js
// Example MDX content that triggers the issue
const mdxContent = `
# Heading

Some text with [link](url)

More content
`;

// When parsing this content, certain constructs are being skipped
const result = compile(mdxContent);
```

The parser seems to be missing or incorrectly handling certain tokens when multiple constructs need to be tried before finding a match.

### Expected behavior

The tokenizer should properly iterate through all available constructs in the list when one fails to match, ensuring that all valid MDX syntax is correctly parsed and no constructs are inadvertently skipped.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
