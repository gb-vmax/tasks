# Bug Report

### Describe the bug
When parsing markdown content with specific character sequences, the parser is incorrectly identifying break points. This causes certain valid markdown constructs to be rejected or parsed incorrectly, particularly when dealing with constructs that have `previous` conditions.

### Reproduction
```js
// Example markdown that triggers the issue
const markdown = `
Some text with special characters that should be parsed correctly.

* List item with preceding content
* Another item
`;

const result = remark().parse(markdown);
// The parser fails to recognize valid break points
```

### Expected behavior
The markdown parser should correctly identify break points and parse all valid markdown constructs, even when they have `previous` conditions that need to be checked. Valid markdown should not be rejected due to incorrect break point detection.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to affect markdown parsing where the parser needs to determine if a character code represents a valid break point in the content. The logic for checking previous conditions appears to be inverted, causing valid constructs to be rejected.

---
Repository: /testbed
