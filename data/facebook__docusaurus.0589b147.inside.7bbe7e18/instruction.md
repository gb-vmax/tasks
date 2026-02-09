# Bug Report

### Describe the bug

I'm encountering an issue with parsing markdown titles/strings that contain backslashes. The parser seems to be stuck in an infinite loop or behaving incorrectly when processing escaped characters within title strings.

### Reproduction

```js
// Example markdown that causes the issue
const markdown = `[link](url "title with \\ backslash")`

// Parser gets stuck or produces unexpected output
const result = remark.parse(markdown)
```

When parsing link titles that contain backslashes, the parser doesn't advance properly through the string. This appears to affect any title/string content with escape sequences.

### Expected behavior

The parser should correctly handle escaped characters in title strings and continue processing the rest of the content without getting stuck. Backslashes should be treated as escape characters and the parser should move to the next character appropriately.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
