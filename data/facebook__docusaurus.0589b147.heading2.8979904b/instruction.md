# Bug Report

### Describe the bug

I'm experiencing an issue with heading elements in MDX. When I use headings in my MDX files, they're not rendering correctly and the structure seems broken. The headings appear to be missing or have incorrect properties.

### Reproduction

```mdx
# My Heading

Some content here

## Subheading

More content
```

When processing this MDX content, the heading nodes don't have the expected structure. It looks like the `type` property is wrong and the `children` property is not being set up correctly.

### Expected behavior

Headings should render properly with:
- Correct `type` field set to "heading"
- Valid `depth` property indicating the heading level
- `children` array properly initialized (even if empty initially)

The heading AST nodes should be compatible with the rest of the MDX processing pipeline.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
