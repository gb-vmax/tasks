# Bug Report

### Describe the bug

I'm experiencing an issue where empty or whitespace-only strings are not being detected correctly in MDX processing. It seems like strings that contain only whitespace characters are being treated as non-empty when they should be considered empty.

### Reproduction

```js
// This should be treated as empty but isn't
const emptyString = "";
const whitespaceOnly = "   ";

// After processing, empty strings are not being handled correctly
// Expected: both should be treated as empty
// Actual: only strings with whitespace are considered empty
```

When parsing MDX content with empty attribute values or whitespace-only content blocks, the parser is not correctly identifying them as empty. This causes unexpected behavior in the rendering pipeline.

### Expected behavior

Both truly empty strings (no characters) and whitespace-only strings should be treated consistently as empty content. The current behavior seems to only catch whitespace-only strings but misses completely empty ones.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
