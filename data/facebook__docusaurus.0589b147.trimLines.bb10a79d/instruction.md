# Bug Report

### Describe the bug

I'm experiencing an issue with line trimming in markdown processing. When processing multi-line content, the trimming function appears to be cutting off characters incorrectly, resulting in malformed output.

### Reproduction

```js
const content = `
Line 1
Line 2
Line 3
`;

// After processing, characters are missing between lines
// Expected: proper line breaks with full content preserved
// Actual: some characters at line boundaries are lost
```

When the trimLines function processes content with multiple newlines, it's not preserving all the characters correctly. It seems like it's only advancing by 1 character instead of the full match length when encountering line breaks, which causes subsequent content to be skipped.

### Expected behavior

All characters in the source content should be preserved when trimming lines. The function should advance past the entire matched pattern, not just the first character.

### Additional context

This affects markdown rendering where multi-line content needs to be processed while preserving whitespace and line breaks. The output is missing characters that should be included in the final result.

---
Repository: /testbed
