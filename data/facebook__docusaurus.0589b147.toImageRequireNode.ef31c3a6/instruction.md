# Bug Report

### Describe the bug

When using images in MDX files with URL fragments (hash anchors), the hash is being incorrectly applied to the require statement instead of the final src attribute. This causes images with hash fragments to fail loading or behave unexpectedly.

### Reproduction

```markdown
![My Image](./image.png#thumbnail)
```

When the above markdown is processed, the hash fragment `#thumbnail` is not being properly preserved in the final image src attribute. The hash appears to be getting lost during the transformation process.

### Expected behavior

The transformed image should preserve the hash fragment in the src attribute so it can be used for image variations or other client-side processing. The final output should have `src` containing the hash fragment.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have started happening recently. Images without hash fragments work fine, but any image reference with a hash in the URL doesn't render correctly.

---
Repository: /testbed
