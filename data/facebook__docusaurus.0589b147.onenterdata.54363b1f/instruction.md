# Bug Report

### Describe the bug

I'm experiencing an issue with text node handling in markdown parsing. When parsing markdown content with consecutive text segments, the text nodes are not being combined correctly and the stack management appears to be broken.

### Reproduction

```js
// Parse markdown with consecutive text content
const markdown = `This is some text that should be combined into a single text node`;

// After parsing, the text nodes are duplicated or incorrectly structured
// Expected: Single text node with combined content
// Actual: Multiple text nodes or incorrect node structure
```

### Expected behavior

When processing consecutive text data in markdown, it should:
1. Check if the last sibling is NOT a text node before creating a new one
2. Push the newly created text node onto the stack (not the parent node)
3. Properly combine consecutive text segments into a single text node

### Current behavior

The parser seems to be creating new text nodes when it shouldn't, or pushing incorrect nodes onto the processing stack. This results in malformed AST output where text content is either duplicated or structured incorrectly.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
