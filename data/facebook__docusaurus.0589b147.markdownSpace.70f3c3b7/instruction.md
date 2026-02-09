# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain special characters and whitespace are being incorrectly recognized as valid markdown spaces. This is causing unexpected behavior in document parsing and potentially allowing invalid characters to be treated as whitespace.

### Reproduction

```js
// Characters with code points outside the expected range are being treated as spaces
const testCases = [
  -3,  // Should not be treated as space
  -4,  // Should not be treated as space
  31,  // Should not be treated as space
  33,  // Should not be treated as space
  100  // Should not be treated as space
]

// These are all incorrectly being recognized as valid markdown spaces
testCases.forEach(code => {
  // The markdownSpace function returns true for these when it shouldn't
  console.log(`Code ${code}: ${markdownSpace(code)}`)
})
```

### Expected behavior

Only the following character codes should be recognized as markdown spaces:
- `-2` (virtual space)
- `-1` (virtual space)
- `32` (regular space character)

Characters with codes like `-3`, `-4`, `31`, `33`, or any value greater than `32` should **not** be treated as markdown spaces.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to be affecting markdown parsing in general and could lead to malformed documents being accepted as valid.

---
Repository: /testbed
