# Bug Report

### Describe the bug

I'm experiencing an infinite loop or hanging behavior when parsing certain MDX content. The parser seems to get stuck and never completes, eventually causing the process to hang or run out of memory.

### Reproduction

```js
// Parsing MDX content with specific token patterns causes the parser to hang
const content = `
# Heading

Some text with line endings and various tokens
`;

// This call never completes
const result = parse(content);
```

The issue appears to be related to how the parser collects and processes events during tokenization. When processing certain combinations of line endings and token types, the loop never terminates.

### Expected behavior

The parser should complete successfully and return the parsed MDX structure without hanging or entering an infinite loop.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This is blocking our build process as it causes the bundler to hang indefinitely. Any help would be appreciated!

---
Repository: /testbed
