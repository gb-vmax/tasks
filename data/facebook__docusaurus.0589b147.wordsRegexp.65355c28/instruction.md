# Bug Report

### Describe the bug

I'm experiencing an issue with keyword matching in MDX content. It seems like words that should be matched as keywords are not being recognized correctly, and partial matches are occurring where they shouldn't.

### Reproduction

When parsing MDX with specific keywords, the regex pattern appears to be matching incorrectly. For example:

```js
// Expected: only exact matches like "import", "export", "const"
// Actual: partial matches or incorrect behavior with word boundaries

const keywords = "import export const";
// The pattern should match these words exactly
// But it's not working as expected
```

### Expected behavior

Keywords should be matched exactly and completely. A keyword like "import" should only match the full word "import", not partial strings or with trailing characters.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
