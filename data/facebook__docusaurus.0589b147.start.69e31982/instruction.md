# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where whitespace handling seems broken. When parsing markdown content, the parser is entering a space token type even when no space character is present, which causes unexpected behavior in the output.

### Reproduction

```js
// Parse markdown with non-space content
const result = remark.parse('text');

// The parser incorrectly enters space token type
// even though the first character is 't', not a space
```

This seems to affect any markdown content that doesn't start with whitespace. The parser appears to be unconditionally entering the space token type before checking if the character is actually a space.

### Expected behavior

The parser should only enter the space token type when it actually encounters a space character. Non-space characters should be handled by the appropriate continuation function without entering the space type first.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
