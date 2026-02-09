# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain constructs at break points are not being handled correctly. It seems like the parser is checking for the wrong condition when determining if a position is at a valid break.

### Reproduction

```js
// When parsing markdown with specific constructs that have a `previous` check
const markdown = `
Some text with special constructs
- list item
- another item
`;

const result = remark().parse(markdown);
// The parser incorrectly identifies break positions
```

### Expected behavior

The parser should correctly identify valid break points by checking if a construct does NOT have a `previous` property OR if the `previous` check passes. Currently it seems to be doing the opposite - it's returning true when `previous` exists or when the check passes, which causes valid breaks to be missed and invalid ones to be accepted.

### Additional context

This affects parsing of various markdown constructs that rely on break detection, particularly those with `previous` validators. The logic appears inverted - constructs that should be allowed at breaks are being rejected and vice versa.

---
Repository: /testbed
