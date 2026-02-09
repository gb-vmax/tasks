# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain inline constructs are not being recognized correctly. It seems like the parser is failing to properly identify valid break points for inline elements.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

// Parse markdown with inline constructs
const result = processor.processSync(`
This is some text with **bold** and *italic* formatting.
Also includes [links](http://example.com) and \`code\`.
`);

console.log(result);
```

When parsing markdown content with multiple inline elements (bold, italic, links, code), the parser doesn't seem to correctly identify where these constructs can start. The behavior is inconsistent - sometimes inline formatting works, sometimes it doesn't, depending on what comes before it in the text.

### Expected behavior

The parser should correctly identify all valid inline constructs regardless of their position in the text. All markdown formatting should be properly recognized and converted.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

This seems to have started recently, possibly related to how the parser checks for valid break points in inline content. Any help would be appreciated!

---
Repository: /testbed
