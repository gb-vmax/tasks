# Bug Report

### Describe the bug

I'm encountering an issue with image reference handling in MDX. When using image references (the `![alt][ref]` syntax), the parser seems to be treating them incorrectly - it's adding reference-related properties to regular images and removing the wrong properties from reference images.

### Reproduction

```markdown
![regular image](./image.png)

![reference image][my-ref]

[my-ref]: ./other-image.png
```

When parsing the above MDX content, the resulting AST nodes have incorrect properties:
- Regular images (with direct URLs) are getting `referenceType` properties they shouldn't have
- Reference images are missing their `identifier` property but have `url` and `title` removed instead

### Expected behavior

- Regular images with URLs should have `url` and `title` properties, not reference-related properties
- Reference images should have `identifier`, `label`, and `referenceType` properties, not `url` and `title`

The logic appears to be inverted - it's treating non-reference images as references and vice versa.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
