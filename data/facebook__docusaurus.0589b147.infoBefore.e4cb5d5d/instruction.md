# Bug Report

### Describe the bug
When using fenced code blocks in MDX without an info string (language identifier), the parser crashes or behaves unexpectedly. This appears to happen when the code fence is opened but no language is specified after the backticks.

### Reproduction
```mdx
```
const example = 'test'
```
```

The above MDX content should be valid - a code block without a language identifier is perfectly valid Markdown/MDX syntax. However, after a recent change, this no longer works correctly.

### Expected behavior
Fenced code blocks without language identifiers should be parsed successfully, just like they are in standard Markdown. The parser should handle the case where the info string is empty or missing.

### Additional context
This affects any MDX document that uses plain code blocks without specifying a language. It's a pretty common pattern in documentation where you just want to show some generic code without syntax highlighting.

---
Repository: /testbed
