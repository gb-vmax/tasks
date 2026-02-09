# Bug Report

### Describe the bug

I'm experiencing an issue with MDX link and image parsing where the `alt` text and `children` seem to be assigned to the wrong node types. When I use reference-style links and images in my MDX content, the output is incorrect - links are getting `alt` properties (which should only be for images) and images are getting `children` arrays (which should only be for links).

### Reproduction

```mdx
This is a [reference link][ref]

This is a ![reference image][ref]

[ref]: /path/to/resource
```

When parsing the above MDX content, the resulting AST has:
- Link nodes with an `alt` property instead of `children`
- Image nodes with `children` array instead of an `alt` string

### Expected behavior

- Link nodes should have a `children` array containing the link text
- Image nodes should have an `alt` string property containing the alt text

The logic appears to be reversed - what should apply to links is being applied to images and vice versa.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
