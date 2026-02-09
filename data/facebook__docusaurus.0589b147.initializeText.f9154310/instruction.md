# Bug Report

### Describe the bug

I'm experiencing an infinite loop or stack overflow when parsing certain MDX content. The parser seems to get stuck in an endless recursion and eventually crashes with a "Maximum call stack size exceeded" error.

### Reproduction

```js
// This causes the parser to hang/crash
const mdxContent = `
Some text content here
`;

compile(mdxContent); // Results in stack overflow
```

The issue appears to happen with basic text content. The parser enters an infinite recursive state and never completes.

### Expected behavior

The MDX content should parse successfully without causing stack overflow errors. Text content should be processed normally.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems like a regression as similar content was parsing fine before. The parser appears to be recursively calling itself indefinitely instead of properly consuming and advancing through the text.

---
Repository: /testbed
