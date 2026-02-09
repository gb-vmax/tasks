# Bug Report

### Describe the bug

I'm experiencing an issue with JSX flow parsing in MDX where the parser crashes when processing certain JSX elements. The error seems to be related to how character codes are being handled in the tokenizer.

### Reproduction

```jsx
<Component />
```

When trying to parse basic JSX flow tags, the parser throws an error. This happens with both self-closing tags and regular opening tags. The issue appears to be in the `start2` function of the JSX flow tokenizer where it's trying to call `.toString()` on a character code.

### Expected behavior

The JSX elements should parse correctly without errors. Basic JSX syntax like `<Component />` or `<div>content</div>` should be tokenized properly.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This is blocking my ability to use MDX in my project. Any help would be appreciated!

---
Repository: /testbed
