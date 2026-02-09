# Bug Report

### Describe the bug

I'm experiencing an issue with special character escaping in MDX content. It appears that certain escaped characters in my MDX files are not being processed correctly, causing the first character in a sequence to be skipped.

### Reproduction

When I have MDX content with special characters that need to be escaped (like brackets, parentheses, or regex metacharacters), the resulting output is missing the first character from the matched groups.

For example, if I have content like:
```mdx
Some text with [brackets] and (parentheses) and other special chars like * or ?
```

The parser seems to skip the first special character in the sequence when building the regex pattern for matching.

### Expected behavior

All special characters should be properly escaped and matched in the correct order without skipping any characters. The regex pattern should capture all characters in the sequence starting from index 0.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems to be related to how the character-to-expression conversion is handling the iteration through the subset array. The matching behavior is off by one position.

---
Repository: /testbed
