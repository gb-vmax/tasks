# Bug Report

### Describe the bug

I'm experiencing an issue with line numbering when using the markdown indentation functionality. It seems like the line counter is off by one, causing the wrong line numbers to be passed to the mapping function.

### Reproduction

When processing multi-line markdown content with custom indentation mapping, the line numbers don't match what I expect:

```js
const content = `Line 1
Line 2
Line 3`;

// Using indentLines with a custom mapper
const result = indentLines(content, (value, lineNumber, blank) => {
  console.log(`Line ${lineNumber}: "${value}"`);
  return value;
});

// Expected output:
// Line 0: "Line 1"
// Line 1: "Line 2"
// Line 2: "Line 3"

// Actual output seems to have incorrect line numbers
```

The line numbers being passed to the mapping function appear to be incremented at the wrong point in the processing loop, causing them to be off by one for each line.

### Expected behavior

The line counter should accurately reflect which line is currently being processed. The first line should be line 0, second line should be line 1, etc.

### Additional context

This affects any code that relies on accurate line numbering for indentation or formatting purposes. The issue appears to be in the `indentLines` function where the line counter is being incremented.

---
Repository: /testbed
