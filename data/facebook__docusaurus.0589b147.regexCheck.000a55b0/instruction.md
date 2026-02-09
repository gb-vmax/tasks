# Bug Report

### Describe the bug

I'm encountering an issue with character code validation in the markdown parser. When processing certain unicode characters, the parser is throwing errors because it's receiving string characters instead of character codes, but the validation logic isn't handling this correctly.

### Reproduction

```js
// This breaks when the input is a string character instead of a character code
const code = 'a'; // string character
regexCheck(/\s/)(code); // Should handle this gracefully

// Previously worked with character codes
const charCode = 97; // numeric character code
regexCheck(/\s/)(charCode); // This works fine
```

The issue occurs when the `check` function receives a string character directly instead of a numeric character code. The current validation logic expects numeric codes but doesn't properly handle string inputs.

### Expected behavior

The regex check should work consistently whether it receives character codes (numbers) or actual string characters. The function should either:
1. Accept both types of input and handle them appropriately, or
2. Fail gracefully with a clear error message

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
