# Bug Report

### Describe the bug

I'm experiencing an issue with markdown line ending detection. When processing markdown content with certain line break characters, they're not being recognized correctly, which causes the parser to treat line breaks as regular text instead of actual line endings.

### Reproduction

```js
const text = `Line 1
Line 2
Line 3`;

// Parser doesn't recognize line breaks correctly
// Lines are being concatenated instead of being treated as separate lines
```

Also happens with different types of line separators (like Unicode line/paragraph separators). The markdown processor seems to be using an incorrect check for what constitutes a valid line ending.

### Expected behavior

All valid markdown line ending characters should be properly detected:
- Line Feed (LF, code 10)
- Carriage Return (CR, code 13)  
- Unicode Line Separator (code 8232)
- Unicode Paragraph Separator (code 8233)

The parser should correctly identify these as line breaks and process the markdown accordingly, splitting content into separate lines/paragraphs.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
