# Bug Report

### Describe the bug

I'm encountering an issue with parsing bigint literals in the MDX parser. When parsing bigint values, the `raw` property seems to be capturing incorrect characters, which causes the `bigint` property to contain extra or incorrect digits.

### Reproduction

```js
// Parse a bigint literal like 123n
const result = parse('123n');

// The bigint property contains an unexpected value
// Expected: '123'
// Actual: includes incorrect character(s)
```

When the parser processes bigint literals (numbers ending with 'n'), the extracted bigint string value doesn't match what was actually written in the source code.

### Expected behavior

The `bigint` property should contain only the numeric digits from the source, without any extra characters. For example, parsing `123n` should result in a bigint value of `'123'`, and parsing `456_789n` should result in `'456789'` (with underscores removed as expected).

### Additional context

This appears to be related to how the `raw` slice is being extracted from the input. The timing of when the slice happens relative to the parser position seems off, causing the wrong substring to be captured.

---
Repository: /testbed
