# Bug Report

### Describe the bug

I'm experiencing an issue with MDX image reference handling. When using images with reference-style syntax (like `![alt][ref]`), the parser seems to be treating them incorrectly - it's applying reference properties to direct images and vice versa.

### Reproduction

```markdown
![Direct image](./path/to/image.png)

![Reference image][my-ref]

[my-ref]: ./path/to/ref-image.png
```

When parsing the above MDX content, the direct image (with URL in parentheses) gets treated as if it's a reference-style image, and the actual reference-style image gets treated like a direct image. The `url` and `title` properties are being deleted from the wrong nodes, and `identifier`/`label` properties are also being misapplied.

### Expected behavior

- Direct images with `![alt](url)` syntax should have `url` and `title` properties preserved, with no `identifier` or `label`
- Reference-style images with `![alt][ref]` syntax should have `identifier`, `label`, and `referenceType` properties, with `url` and `title` removed

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken after a recent update. The logic for determining whether an image is a reference or not appears to be inverted.

---
Repository: /testbed
