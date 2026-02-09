# Bug Report

### Describe the bug

Markdown parsing is not working correctly for blank lines. When processing documents with whitespace, the parser seems to be mishandling lines that contain only spaces or are completely empty.

### Reproduction

```js
const markdown = `
First paragraph

Second paragraph
`;

// Parse the markdown
const result = processor.parse(markdown);

// The blank line between paragraphs is not being recognized correctly
// Expected: Two separate paragraph nodes
// Actual: Incorrect parsing behavior
```

Another case that fails:

```js
const markdown = `
    
Next line
`;

// Lines with only spaces should be treated as blank lines
// but they're being processed incorrectly
```

### Expected behavior

Blank lines (whether completely empty or containing only whitespace) should be properly recognized and handled during markdown parsing. This is essential for correctly separating paragraphs and other block-level elements.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
