# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. When using backticks in the info string of a fenced code block, the parser is not handling them correctly and appears to be accepting invalid syntax that should be rejected.

### Reproduction

```markdown
```javascript`extra
const code = 'test';
```
```

The above markdown contains a backtick character within the info string (after "javascript"). This should be treated as invalid syntax, but it seems to be getting parsed without errors.

### Expected behavior

Fenced code blocks with backtick characters in the info string should be rejected as invalid markdown syntax. The parser should not accept info strings that contain the same character used as the fence marker.

### Additional context

This appears to affect code blocks that use backticks as fence markers. The info string (the part after the opening fence that typically specifies the language) should not contain backtick characters when backticks are used as the fence delimiter.

---
Repository: /testbed
