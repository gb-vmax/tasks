# Bug Report

### Describe the bug

I'm experiencing an issue with label/link parsing in MDX where the offset calculation appears to be incorrect. When processing label ends (for images and links), the resolver is not properly accounting for the token boundaries, which causes parsing errors or unexpected behavior.

### Reproduction

```js
// Example MDX content that triggers the issue
const mdxContent = `
![alt text](image.jpg)
[link text](url)
`

// The label end resolution doesn't correctly handle the offset
// between image labels and link labels
```

When parsing MDX content with both image and link labels, the offset tracking seems off. The issue manifests when:
1. Processing nested or adjacent label structures
2. Resolving label end tokens
3. The `_balanced` property check is involved

### Expected behavior

The label end resolver should correctly calculate offsets for both `labelImage` and `labelLink` token types, maintaining proper balance tracking and token boundaries.

### System Info
- MDX version: 3.0.0
- Parser: micromark-based

---
Repository: /testbed
