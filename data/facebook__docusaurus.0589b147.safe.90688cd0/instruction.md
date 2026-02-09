# Bug Report

### Describe the bug

I'm experiencing an issue with escaping special characters in markdown text. When there are special characters at the beginning of a string or adjacent to other special characters, they're not being escaped properly. This results in missing or incorrectly positioned characters in the output.

### Reproduction

```js
const input = "!test";
// Expected: "!test" or "\!test" 
// Actual: "test" (the first character is missing)

const input2 = "!!double";
// Expected: "!!double" or "\!\!double"
// Actual: Characters are not escaped correctly
```

It seems like the issue occurs specifically when:
1. A special character is at the very start of the string (position 0)
2. Multiple special characters appear consecutively

### Expected behavior

Special characters should be properly escaped or preserved in the output, regardless of their position in the string. The first character should not be skipped.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
