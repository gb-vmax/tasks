# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. When I try to use backticks in the info string of a code fence, the parser seems to get stuck in an infinite loop or doesn't properly handle the input.

### Reproduction

```markdown
```javascript`
console.log('test');
```
```

When parsing markdown with a backtick character in the language identifier/info string (like `javascript`), the parser doesn't reject it as expected and continues processing indefinitely.

### Expected behavior

The parser should properly reject fenced code blocks that have backticks in their info string, as this is invalid markdown syntax. The info string should not contain the same character used as the fence marker.

### Additional context

This seems to affect the tokenization logic for code fences. The issue appears when the fence marker character (backtick) appears in the info string portion of the code block declaration.

---
Repository: /testbed
