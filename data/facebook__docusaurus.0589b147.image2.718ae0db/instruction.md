# Bug Report

### Describe the bug

After a recent update, image nodes are being generated with incorrect type and default values. When parsing MDX content with images, the generated AST nodes have `type: "img"` instead of `type: "image"`, and the `alt` attribute defaults to an empty string `""` instead of `null`.

### Reproduction

```js
// Parse MDX content with an image
const result = compile('![](image.png)');

// The image node now has:
// - type: "img" (should be "image")
// - alt: "" (should be null)
```

When processing MDX files that contain images, the AST structure is different from what's expected. This breaks compatibility with tools and plugins that rely on the standard MDX image node format.

### Expected behavior

Image nodes should have:
- `type: "image"` (not "img")
- `alt: null` when no alt text is provided (not empty string)

This was working correctly in previous versions and the change breaks existing MDX processing pipelines.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
