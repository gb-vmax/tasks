# Bug Report

### Describe the bug

I'm experiencing an issue with image link parsing in markdown. When trying to use image syntax like `![alt text](url)`, the parser seems to be behaving incorrectly and the image markers are not being processed as expected.

### Reproduction

```js
const markdown = '![test image](https://example.com/image.png)'

// Parse the markdown
const result = parser.parse(markdown)

// The labelImage token structure appears malformed
// Expected proper nesting of labelImageMarker tokens
```

### Expected behavior

Image links should be parsed correctly with proper token structure. The `labelImageMarker` should be entered and exited in the correct order, and the `labelImage` token should remain open until the full image syntax is processed.

### Additional context

This seems to affect how images are rendered in the final output. The token tree structure for image syntax doesn't match what's expected, which could cause issues downstream in the rendering pipeline.

---
Repository: /testbed
