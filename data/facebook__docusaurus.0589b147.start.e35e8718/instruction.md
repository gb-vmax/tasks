# Bug Report

### Describe the bug

I'm encountering an issue with markdown link parsing where the AST structure for link labels appears to be malformed. When parsing markdown links, the generated syntax tree has duplicate `labelLink` exit events without a corresponding entry event.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = '[example](https://example.com)';
const ast = processor.parse(markdown);

// The AST structure for the link label is incorrect
// Expected: enter labelLink -> enter labelMarker -> exit labelMarker -> exit labelLink
// Actual: enter labelMarker -> exit labelMarker -> exit labelLink -> exit labelLink (duplicate exit!)
```

### Expected behavior

The tokenizer should properly enter and exit the `labelLink` state exactly once. Each `enter` event should have a corresponding `exit` event, and there should not be duplicate exit calls for the same token type.

### Additional context

This seems to affect the parsing of all markdown links. The AST becomes unbalanced which could cause issues with transformers or plugins that rely on the correct nesting structure of tokens.

---
Repository: /testbed
