# Bug Report

### Describe the bug

I've noticed some incorrect behavior with lazy continuation detection in markdown parsing. When processing block containers, the parser seems to be marking lines as lazy incorrectly, which affects how nested block structures are parsed.

### Reproduction

```js
const markdown = `
> Quote line 1
  Continuation line
> Quote line 2
`;

const result = remark().parse(markdown);
// The continuation line is being treated incorrectly
```

The issue appears when a line continues a block container but isn't actually lazy. The parser is setting the lazy flag backwards - it marks lines as lazy when they should be non-lazy and vice versa.

### Expected behavior

Lines that are actual continuations of a container (not lazy) should be marked as `lazy: false`, while lines that are lazy continuations should be marked as `lazy: true`. Currently this seems to be inverted.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This is affecting nested blockquotes and list parsing where lazy continuation matters for correct structure.

---
Repository: /testbed
