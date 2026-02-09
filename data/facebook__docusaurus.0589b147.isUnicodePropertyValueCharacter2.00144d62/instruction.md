# Bug Report

### Describe the bug

I'm encountering a critical parsing error when processing MDX files with Unicode regex patterns. The parser crashes with a syntax error when it encounters certain Unicode property escapes in regular expressions.

### Reproduction

```js
const mdxContent = `
---
title: Test
---

Some text with a regex pattern that uses Unicode properties like \p{Letter} or \p{Number}.
`;

// Parser fails to process this content
```

When trying to parse MDX content that contains Unicode property escapes in regex patterns, the parser throws an error and fails to process the file. This seems to affect any content using Unicode character classes.

### Expected behavior

The parser should correctly handle Unicode property escapes in regular expressions without throwing errors. MDX files containing these patterns should be parsed successfully.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This is blocking our ability to use certain regex patterns in our documentation. Any help would be appreciated!

---
Repository: /testbed
