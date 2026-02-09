# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain content appears to be processed multiple times or gets stuck in an infinite loop. The parser seems to hang or produce duplicate output when processing specific markdown structures.

### Reproduction

```js
// Parse markdown with nested structures
const result = remark.parse(`
# Heading

Some text with **bold** and *italic*.

- List item 1
- List item 2
`);

// Parser appears to hang or produce unexpected output
```

### Expected behavior

The markdown should be parsed once and produce the correct AST structure without any duplication or hanging. Each chunk of the input should be processed exactly once.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have started happening recently. The parser either hangs indefinitely or produces corrupted output where some tokens appear multiple times in the result.

---
Repository: /testbed
