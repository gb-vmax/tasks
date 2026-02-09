# Bug Report

### Describe the bug

After a recent update, the markdown parser is incorrectly treating certain characters as whitespace. This is causing issues with parsing markdown content that contains special characters or control codes.

### Reproduction

```js
// Characters in the range between -2 and 32 are now all treated as whitespace
// This includes characters like:
// - Control characters (codes 0-31)
// - Characters that should NOT be considered markdown whitespace

const parser = createMarkdownParser();
const result = parser.parse('text\x01content'); // \x01 is character code 1

// The parser now incorrectly treats \x01 as whitespace and may split or 
// improperly handle the content
```

The issue appears to be in the `markdownSpace` function which is now using a range check instead of explicitly checking for the specific whitespace character codes (-2, -1, and 32).

### Expected behavior

Only the specific markdown whitespace characters (codes -2, -1, and 32) should be treated as whitespace. Other characters in that range, especially control characters, should be handled according to their actual character type.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
