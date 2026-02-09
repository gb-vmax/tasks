# Bug Report

### Describe the bug

I've encountered an issue with keyword matching in MDX files. It seems like keywords are being matched in the middle of words instead of only matching complete words. This is causing false positives where parts of longer identifiers or variable names are incorrectly treated as keywords.

### Reproduction

When parsing MDX content with words that contain keyword substrings, the parser incorrectly identifies them as keywords:

```js
// This should NOT be treated as a keyword match
const myimportant = 'value'

// But it's being matched because it contains 'import'
```

Similarly, words like `exportData`, `returnValue`, or any identifier containing reserved words as substrings are being incorrectly flagged.

### Expected behavior

Keywords should only match when they appear as complete, standalone words - not as substrings within larger identifiers. The regex should enforce word boundaries so that:
- `import` matches as a keyword
- `importData` does NOT match
- `myimport` does NOT match

### System Info
- Using remark-mdx 3.0.0
- Node version: 18.x

This is affecting MDX parsing and causing unexpected behavior in our documentation site. Any identifiers that happen to contain JavaScript keywords are being treated incorrectly.

---
Repository: /testbed
