# Bug Report

### Describe the bug

Character references in markdown are not being parsed correctly. When processing text with HTML entities or numeric character references (like `&amp;`, `&#123;`, etc.), the parser appears to get stuck in an infinite loop or fails to properly tokenize the content.

### Reproduction

```js
const text = 'This is a test with &amp; character reference';
// Parser hangs or produces incorrect output

const numericRef = 'Numeric reference: &#65; should work';
// Also fails to parse correctly
```

### Expected behavior

Character references should be properly tokenized and converted. For example:
- `&amp;` should be recognized as an ampersand entity
- `&#65;` should be recognized as the letter 'A'
- The parser should complete successfully without hanging

### System Info
- remark version: 15.0.1

---
Repository: /testbed
