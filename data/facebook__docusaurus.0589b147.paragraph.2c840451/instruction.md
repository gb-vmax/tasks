# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where the order of operations seems to be incorrect when processing paragraph nodes. The state tracking appears to be happening in the wrong sequence, which could lead to incorrect context being maintained during the markdown-to-AST conversion process.

### Reproduction

When parsing markdown content with paragraphs, the internal state management for "phrasing" context is being entered and exited at the wrong times relative to when the actual container phrasing content is being processed.

```js
// Example markdown that triggers the issue
const markdown = `
This is a paragraph with some text.

Another paragraph here.
`;

// The phrasing state is being set up after the content 
// has already been processed, rather than before
```

### Expected behavior

The state tracking should enter the "phrasing" context *before* processing the container phrasing content, and exit *after* the content has been processed. This ensures that the correct context is available during the processing of paragraph content.

The current implementation processes the content first and then sets up the context, which is backwards from what it should be.

### System Info
- remark version: 15.0.1
- Affected module: mdast-util-to-markdown

---
Repository: /testbed
