# Bug Report

### Describe the bug

Image paths are not resolving correctly in MDX files. When using images with URL hash fragments or query parameters, the generated require paths are broken, causing images to fail loading.

### Reproduction

```md
![Alt text](./images/photo.png#thumbnail)
![Another image](./images/diagram.png?width=500)
```

When these images are processed, they don't load correctly. The relative path calculation seems reversed, and the hash/search parameters are being swapped in the require string.

### Expected behavior

Images with hash fragments and query parameters should resolve and load correctly. The relative path should be calculated from the MDX file to the image, not the other way around.

For example:
- `./images/photo.png#thumbnail` should keep the hash fragment in the correct position
- `./images/diagram.png?width=500` should preserve the query parameters properly

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have broken recently, images that previously worked are now showing as missing/broken links.

---
Repository: /testbed
