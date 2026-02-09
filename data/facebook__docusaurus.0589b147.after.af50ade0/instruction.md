# Bug Report

### Describe the bug

I'm encountering an issue with blank line parsing in markdown content. It seems like blank lines are not being recognized correctly, which is causing unexpected behavior when processing markdown documents.

### Reproduction

```js
const markdown = `
First paragraph

Second paragraph
`;

// Process the markdown
const result = remark().parse(markdown);

// The blank line between paragraphs is not being handled correctly
// causing the two paragraphs to merge or be processed incorrectly
```

### Expected behavior

Blank lines (lines containing only whitespace or line endings) should be properly tokenized and recognized as separators between content blocks. Currently, it appears that lines with line ending characters are being rejected when they should be accepted, leading to incorrect parsing of paragraph breaks and other block-level structures.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
