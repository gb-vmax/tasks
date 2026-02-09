# Bug Report

### Describe the bug

I'm experiencing issues with link destinations in markdown parsing. When using backslash escapes in enclosed link destinations (angle brackets), the parser doesn't handle them correctly. Additionally, raw link destinations without angle brackets seem to terminate prematurely or not at all depending on the content.

### Reproduction

```js
// Case 1: Backslash escape in enclosed destination
const markdown1 = '[link](<https://example.com/path\\>with\\>brackets>)'

// Case 2: Raw destination with parentheses
const markdown2 = '[link](https://example.com/path(with)parens)'
```

The first case with backslash escapes in the enclosed destination doesn't parse correctly - the escaped characters aren't being recognized as they should be.

The second case with raw destinations (no angle brackets) has problems when the URL contains parentheses or spaces - the destination either ends too early or continues when it shouldn't.

### Expected behavior

- Backslash escapes like `\>` and `\<` should be properly recognized inside angle-bracketed link destinations
- Raw link destinations should correctly terminate when encountering unbalanced parentheses or whitespace
- The parser should handle both enclosed and raw destination formats according to the CommonMark spec

### System Info
- remark version: 15.0.1
- Node: 18.x

---
Repository: /testbed
