# Bug Report

### Describe the bug

I'm encountering an issue with the `indentLines` function in the remark markdown processor. When processing markdown content with indentation, the line counter and empty line detection seem to be producing incorrect results.

### Reproduction

```js
const remark = require('remark');

const markdown = `
First line
  Indented line
    More indented

Last line
`;

const processor = remark();
const result = processor.processSync(markdown);
```

When the `indentLines` function processes this content, the line number tracking appears to be broken. The function is supposed to track which line number it's processing and whether a line is empty, but it's not working as expected.

### Expected behavior

The indentation mapping function should receive:
1. The correct line content
2. The accurate line number being processed  
3. A proper boolean indicating if the line is empty (true/false)

Instead, it seems like the wrong values are being passed to the mapping function, which causes issues with markdown formatting that relies on line numbers or needs to handle empty lines differently.

### System Info
- remark version: 15.0.1
- Node.js version: Latest

This is affecting markdown files that have complex indentation patterns or need accurate line number tracking for proper rendering.

---
Repository: /testbed
