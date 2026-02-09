# Bug Report

### Describe the bug

I'm experiencing an issue with markdown emphasis (bold/italic) parsing after a recent update. The emphasis markers (asterisks and underscores) are not being correctly recognized in certain contexts, particularly when dealing with punctuation or special characters adjacent to the markers.

### Reproduction

```js
// These patterns are not being parsed correctly:
const markdown1 = "This is *italic* text.";
const markdown2 = "This is _also italic_ text.";
const markdown3 = "**bold** followed by punctuation.";

// The emphasis markers seem to be ignored or incorrectly applied
// when they appear next to certain characters
```

When processing markdown with emphasis markers adjacent to punctuation or in specific character combinations, the opening and closing markers are not being matched properly. The text either renders without any emphasis or the emphasis extends beyond where it should stop.

### Expected behavior

Emphasis markers should be correctly identified and matched regardless of adjacent punctuation or character types. Both asterisks (`*`, `**`) and underscores (`_`, `__`) should work consistently for italic and bold text formatting.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
