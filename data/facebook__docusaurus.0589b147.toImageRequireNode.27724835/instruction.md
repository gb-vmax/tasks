# Bug Report

### Describe the bug

Image URLs in MDX files are not getting the correct hash appended to them. This causes issues with cache busting - when images are updated, browsers may still serve the old cached version because the URL hasn't changed.

### Reproduction

```mdx
![My Image](./my-image.png)
```

After the MDX loader processes this, the generated `src` attribute should include a hash based on the image content (e.g., `require('./my-image.png?abc123')`), but the hash is missing.

### Expected behavior

Images should have content hashes appended to their URLs to enable proper cache invalidation. When an image file changes, the hash in the URL should also change, forcing browsers to fetch the new version.

### Additional context

This seems to affect all images referenced in MDX files. The require statements are generated correctly but without the hash parameter.

---
Repository: /testbed
