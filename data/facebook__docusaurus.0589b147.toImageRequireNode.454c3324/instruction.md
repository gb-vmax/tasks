# Bug Report

### Describe the bug

Image links with URL fragments (hash anchors) are not working correctly in MDX files. When using an image with a hash in the URL, the hash and search parameters get swapped, causing the image to not load properly or lose its query parameters.

### Reproduction

```markdown
![Alt text](./image.png?width=500#anchor)
```

When this markdown image is processed, the hash and search parameters are reversed in the require string and the src attribute. The search parameter ends up in the require string where the hash should be, and vice versa.

### Expected behavior

The image should load correctly with both the query parameters and hash fragment preserved in their correct positions:
- Query parameters (`?width=500`) should be part of the require string
- Hash fragment (`#anchor`) should be passed to the `assetRequireAttributeValue` function

Currently it appears these are being swapped, which breaks image loading when both are present.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
