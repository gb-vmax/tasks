# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain constructs seem to be getting resolved incorrectly. When parsing markdown documents with specific patterns, the tokenizer appears to be processing events in an unexpected way.

### Reproduction

```js
const remark = require('remark');

const markdown = `
# Heading

Some text with **bold** and *italic*.

- List item 1
- List item 2
`;

const result = remark().parse(markdown);
// The parsed AST structure is incorrect for certain nested constructs
```

### Expected behavior

The markdown should be parsed correctly with all constructs (headings, emphasis, lists) properly resolved and represented in the AST. However, it seems like some events are being sliced or resolved from the wrong position, leading to malformed output.

### Additional context

This appears to affect documents with multiple nested or adjacent formatting constructs. Simple markdown without complex nesting seems to work fine, but once you have overlapping or consecutive constructs, the parsing becomes unreliable.

---
Repository: /testbed
