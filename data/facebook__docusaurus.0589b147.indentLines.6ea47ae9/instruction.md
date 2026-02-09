# Bug Report

### Describe the bug

I'm encountering an issue with the `indentLines` function where the line numbers passed to the mapping function seem to be off by one. When processing multi-line text, the callback receives incorrect line indices, which causes problems when trying to apply line-specific formatting or transformations.

### Reproduction

```js
const text = "line 1\nline 2\nline 3";

const result = indentLines(text, (value, lineNumber, isBlank) => {
  console.log(`Line ${lineNumber}: "${value}"`);
  return value;
});

// Current output:
// Line 1: "line 1"
// Line 2: "line 2"
// Line 3: "line 3"

// Expected output:
// Line 0: "line 1"
// Line 1: "line 2"
// Line 2: "line 3"
```

The line numbering starts at 1 instead of 0, which is inconsistent with typical array indexing and makes it difficult to correlate with line positions in the original text.

Additionally, the third parameter (blank line indicator) seems to always be `false` for the first line regardless of whether it's actually blank or not.

### Expected behavior

The line number should start at 0 for the first line and increment correctly for subsequent lines. The blank line indicator should accurately reflect whether each line is empty.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
