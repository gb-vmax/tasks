# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where certain constructs fail to parse correctly. It seems like the parser is not properly restoring state when trying alternative parsing strategies, which causes it to skip valid constructs or produce incorrect output.

### Reproduction

```js
const remark = require('remark');

const markdown = `
Some text with **bold** and _italic_.

- List item 1
- List item 2
`;

const result = remark.parse(markdown);
console.log(result);
```

When parsing markdown with multiple nested or sequential constructs, the parser doesn't handle fallback cases properly. The state restoration seems to be missing when a construct fails to match, leading to incorrect parsing results or skipped content.

### Expected behavior

The parser should properly restore its state when a construct fails to match and try the next available construct. All valid markdown should be parsed correctly even when the parser needs to backtrack and try alternative parsing strategies.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
