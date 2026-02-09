# Bug Report

### Describe the bug

I'm experiencing an issue with character escaping in regex patterns. When processing certain special characters, they're not being captured correctly in the resulting regular expression groups.

### Reproduction

```js
// When using special characters that need escaping
const chars = ['$', '*', '?'];
const result = charactersToExpression(chars);

// The regex pattern generated doesn't capture groups as expected
// Characters are matched but not captured properly
```

The issue seems to be related to how the regular expression groups are constructed. The pattern is matching the characters but not capturing them in the way that's needed for further processing.

### Expected behavior

Special characters should be properly escaped AND captured in regex groups so they can be extracted and used in subsequent operations. The current behavior is causing issues with text replacement and character substitution operations.

### Additional context

This affects any workflow that relies on capturing specific special characters from text, particularly when dealing with markdown or other markup languages that use these characters as syntax elements.

---
Repository: /testbed
