# Bug Report

### Describe the bug

I'm experiencing an issue with SVG elements in MDX files. When I use SVG components in my MDX content, the attributes are not being processed correctly. It seems like the attributes are being ignored or handled improperly.

### Reproduction

```mdx
<svg width="100" height="100">
  <circle cx="50" cy="50" r="40" fill="red" />
</svg>
```

When rendering this SVG in an MDX file, the attributes on both the `<svg>` and `<circle>` elements don't appear to be working as expected. The SVG renders but without the proper dimensions or styling.

Also noticed that mixed-case SVG element names like `<SVG>` or `<Svg>` might not be recognized correctly.

### Expected behavior

SVG elements and their attributes should be processed and rendered correctly in MDX files, just like regular HTML/JSX elements. The width, height, and other SVG-specific attributes should be preserved and applied.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
