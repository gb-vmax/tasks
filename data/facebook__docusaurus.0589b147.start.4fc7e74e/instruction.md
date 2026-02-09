# Bug Report

### Describe the bug

Image link syntax in markdown is not being parsed correctly. When trying to use image links like `![alt text](url)`, the parser seems to be failing or producing incorrect output.

### Reproduction

```js
const markdown = '![test image](https://example.com/image.png)'
const result = remark.parse(markdown)

// The parsed AST is malformed or the image node is not created properly
console.log(result)
```

### Expected behavior

The markdown parser should correctly handle image syntax `![alt](url)` and produce a valid AST with an image node. The image marker tokens should be properly opened and closed.

### Additional context

This appears to affect all image links in markdown documents. Regular links with `[text](url)` work fine, but adding the `!` prefix for images causes issues.

---
Repository: /testbed
