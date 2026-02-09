# Bug Report

### Describe the bug

I'm experiencing an issue with the sync diff algorithm where it seems to be creating an excessive number of block mappings for small strings. The block map generation appears to be processing strings with a rolling window approach even when it shouldn't, which is causing performance issues and potentially incorrect diff results.

### Reproduction

When syncing documents with small text changes, the diff calculation takes significantly longer than expected. For example:

```js
// Simple text comparison that should be fast
const text1 = "Hello World";
const text2 = "Hello Universe";

// The diff operation hangs or takes an unusually long time
const delta = diff(text1, text2);
```

The issue seems to occur specifically when:
1. The text being compared is relatively short (under 100 characters)
2. The block size is small (16 or less)
3. Multiple blocks end up with the same hash value

### Expected behavior

The diff algorithm should efficiently process small text changes without creating redundant block mappings. For short strings with small block sizes, it should use a non-overlapping block strategy instead of a rolling window approach.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started happening recently - the sync operations that used to complete instantly are now noticeably slower.

---
Repository: /testbed
