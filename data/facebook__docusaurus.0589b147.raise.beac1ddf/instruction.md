# Bug Report

### Describe the bug

I'm getting a crash when trying to use the MDX parser with invalid regular expressions. It looks like the error handling for regex validation has been broken somehow.

### Reproduction

```js
// Using remark-mdx to parse content with an invalid regex pattern
const mdx = `
Some content with a regex pattern that's invalid
`;

// Parser crashes instead of raising a proper error
parser.parse(mdx);
```

When the parser encounters an invalid regular expression pattern, it completely crashes instead of providing a helpful error message about what went wrong with the regex.

### Expected behavior

The parser should raise a recoverable error with a message like "Invalid regular expression: /pattern/: [reason]" instead of crashing.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
