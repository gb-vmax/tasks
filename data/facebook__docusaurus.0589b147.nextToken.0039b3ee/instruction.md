# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX parser where whitespace handling seems broken. When parsing MDX content, spaces are being skipped in contexts where they should be preserved, leading to incorrect tokenization.

### Reproduction

```js
const mdx = require('@mdx-js/mdx');

// Parse MDX content with preserved whitespace context
const content = `
<Component>
  Text with   spaces
</Component>
`;

const result = await mdx.compile(content);
// Whitespace is incorrectly stripped in certain contexts
```

### Expected behavior

Whitespace should be preserved in contexts that require it (like inside JSX elements with text content). The parser should respect the `preserveSpace` context flag and only skip whitespace when appropriate.

### Additional context

This appears to affect tokenization - the parser seems to be skipping spaces even when the current context indicates they should be preserved. Also noticing that end-of-file detection might be off by one position, potentially causing issues with parsing files that end without trailing newlines.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest LTS

---
Repository: /testbed
