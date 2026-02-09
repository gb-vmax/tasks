# Bug Report

### Describe the bug

I'm experiencing an issue with text trimming in MDX content. It appears that the first character of the content is being incorrectly removed when processing certain text blocks.

### Reproduction

When parsing MDX content that starts immediately without leading whitespace, the first character gets stripped:

```js
const content = `Hello world
This is a test`;

// After processing through trimLines
// Expected: "Hello world\nThis is a test"
// Actual: "ello world\nThis is a test"
// The 'H' is missing!
```

This seems to happen specifically when the content starts at position 0 in the source string.

### Expected behavior

The trimming function should preserve all content characters and only remove intended whitespace. The first character should not be removed.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
