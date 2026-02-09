# Bug Report

### Describe the bug

I'm experiencing an issue with emphasis (italic) rendering in MDX where the children nodes are not being processed correctly. When I use emphasis syntax in my MDX files, the content inside the emphasis tags appears to be undefined or incorrectly transformed.

### Reproduction

```mdx
This is *italic text* in my document.
```

When this gets processed, the italic text doesn't render properly. It seems like the children of the emphasis element are not being captured correctly during the AST transformation.

### Expected behavior

The emphasis should render correctly with its children intact:
```html
This is <em>italic text</em> in my document.
```

Instead, it appears the children are getting lost or replaced with something else during the transformation process.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. Any help would be appreciated!

---
Repository: /testbed
