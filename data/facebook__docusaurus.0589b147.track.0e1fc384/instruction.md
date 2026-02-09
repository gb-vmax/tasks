# Bug Report

### Describe the bug

I'm experiencing an issue with position tracking in multi-line text parsing. When processing text that contains newlines, the column position calculation seems to be off, and I'm getting undefined values in certain cases.

### Reproduction

```js
const tracker = track({ line: 1, column: 1 });

// Processing multi-line text
const text = "first line\nsecond line\nthird line";
tracker.move(text);

// The column position is calculated incorrectly
// Getting undefined when accessing the tail chunk
```

The issue appears when the text contains line breaks and the position tracker tries to determine the column number for the final position. It seems like there's an off-by-one error when accessing array elements.

### Expected behavior

The position tracker should correctly calculate line and column positions after processing multi-line text without encountering undefined values or incorrect column calculations.

### System Info
- Version: remark@15.0.1
- Node: v18.x

---
Repository: /testbed
