# Bug Report

### Describe the bug
I'm encountering an issue with markdown parsing where content with certain nested structures is being processed incorrectly. It seems like the parser is getting confused when handling subcontent events, leading to malformed output or infinite loops.

### Reproduction
```js
const remark = require('remark');

const markdown = `
# Heading

> Blockquote with nested content
> 
> - List item 1
> - List item 2
`;

const result = remark().parse(markdown);
// Parser hangs or produces incorrect AST structure
```

### Expected behavior
The parser should correctly handle nested content within blockquotes and other container elements, producing a valid AST without hanging or generating malformed structures.

### Additional context
This seems to affect scenarios where there are multiple levels of nesting (like lists inside blockquotes, or other combinations of container elements). The issue appears to be related to how event positions are being tracked during subcontent processing.

---
Repository: /testbed
