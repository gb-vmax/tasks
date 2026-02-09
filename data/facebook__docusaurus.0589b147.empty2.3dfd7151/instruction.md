# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where empty or whitespace-only content is not being handled correctly. When I have content that consists only of whitespace characters, it's not being recognized as empty, which causes unexpected behavior in the rendering output.

### Reproduction

```js
// This should be treated as empty content but isn't
const content = "   ";  // just spaces

// After processing through MDX, this is not being detected as empty
// even though it contains only whitespace
```

Another case:
```js
const contentWithNewlines = "\n\n\n";  // just newlines
// This also fails to be recognized as empty
```

### Expected behavior

Content that contains only whitespace characters (spaces, tabs, newlines) should be treated as empty content, similar to how completely empty strings are handled. The parser should recognize these as empty and handle them accordingly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have started happening recently. Previously, whitespace-only content was being handled the same way as truly empty content.

---
Repository: /testbed
