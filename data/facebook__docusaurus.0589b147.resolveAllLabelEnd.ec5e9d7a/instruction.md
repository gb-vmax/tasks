# Bug Report

### Describe the bug

I'm encountering an issue with parsing markdown links and images. When processing documents with multiple consecutive links or images, some content appears to be getting corrupted or lost during parsing.

### Reproduction

```js
const markdown = `
[link1](url1)[link2](url2)
![image1](img1)![image2](img2)
`

// After parsing, the output is malformed
// Some link/image content is missing or incorrectly processed
```

### Expected behavior

All links and images should be parsed correctly regardless of how many appear consecutively in the document. Each link/image should maintain its full content and structure.

### Additional context

This seems to affect scenarios where you have:
- Multiple links placed directly next to each other
- Multiple images in sequence
- Mixed combinations of links and images without spacing

The parsed output doesn't match what you'd expect from the input markdown. It's like some tokens are being skipped or removed incorrectly during the parsing phase.

---
Repository: /testbed
