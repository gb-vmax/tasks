# Bug Report

### Describe the bug

I'm experiencing an issue with character classification in markdown parsing. It seems like certain punctuation characters are being classified incorrectly, which is causing unexpected behavior when parsing markdown content.

### Reproduction

```js
// When parsing markdown with punctuation at boundaries
const markdown = `**bold**text`;

// The punctuation classification seems wrong
// Expected: punctuation should be classified as type 2
// Actual: it's being classified as type 1
```

Another case:
```js
const markdown = `text_with_underscores_here`;

// Underscores adjacent to text aren't being handled correctly
```

### Expected behavior

Punctuation characters should be properly classified as type 2 for correct emphasis/strong delimiter processing. Currently it seems like the classification is returning the wrong value for punctuation characters, causing them to be treated differently than they should be.

### System Info
- remark version: 15.0.1
- Browser: N/A (Node.js environment)

This is affecting markdown parsing where emphasis markers and other punctuation need to be correctly identified for proper formatting.

---
Repository: /testbed
