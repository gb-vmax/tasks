# Bug Report

### Describe the bug

I'm experiencing an issue with code fence parsing where fenced code blocks are not being terminated correctly when they end at the end of a file (without a trailing newline). The parser seems to be handling the null character (end of file) incorrectly.

### Reproduction

```markdown
# Document

```js
const x = 1;
```
```

When the markdown file ends immediately after the closing fence without a newline character, the code block is not properly recognized/closed.

### Expected behavior

Code fences should be properly closed regardless of whether there's a trailing newline after the closing fence or if the fence is at the end of the file. Both of these should parse correctly:

1. Code fence with trailing newline
2. Code fence at EOF without trailing newline

The parser should handle the `null` (EOF) character the same way it handles line endings when closing a code fence.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
