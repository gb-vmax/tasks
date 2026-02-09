# Bug Report

### Describe the bug

Images are being incorrectly parsed as image references when they should be treated as regular images. The logic for determining whether an image is a reference or not appears to be inverted - non-reference images are getting reference properties added, while actual reference images are having their reference properties removed.

### Reproduction

```markdown
![alt text](https://example.com/image.png)
```

When parsing the above markdown, the image is being treated as an image reference instead of a regular image. The resulting AST node has `referenceType` set and the `url` property is deleted, even though this is clearly a standard image with a URL.

Similarly, actual image references like:

```markdown
![alt text][ref]

[ref]: https://example.com/image.png
```

Are being treated as regular images with the `identifier` and `label` properties removed.

### Expected behavior

Regular images with URLs should be parsed as `image` nodes with `url` and `title` properties intact. Image references should be parsed as `imageReference` nodes with `referenceType`, `identifier`, and `label` properties.

The reference detection logic seems to be backwards - it's applying reference handling to non-references and vice versa.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
