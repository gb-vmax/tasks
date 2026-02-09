# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where whitespace handling appears to be broken. When parsing markdown content with spaces, the parser seems to be calling callbacks in the wrong order or processing non-space characters incorrectly.

### Reproduction

```js
// Parse markdown with leading spaces
const markdown = "   some text with leading spaces";
const result = parseMarkdown(markdown);

// The parser behaves unexpectedly - spaces are not being 
// properly consumed before entering the type state
```

When the parser encounters whitespace at the start of content, it should:
1. Check if it's a markdown space
2. Enter the type state
3. Process the space character

But instead, it seems to be calling the success callback (`ok3`) prematurely or processing characters that aren't spaces through the wrong code path.

### Expected behavior

The parser should correctly handle leading/trailing whitespace in markdown content. Spaces should be properly identified and consumed before moving to the next parsing state.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

This is causing issues with parsing markdown tables and other GFM features that rely on proper whitespace handling.

---
Repository: /testbed
