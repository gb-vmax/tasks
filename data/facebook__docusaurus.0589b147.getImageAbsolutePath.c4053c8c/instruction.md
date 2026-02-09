# Bug Report

### Describe the bug

I'm experiencing an issue with image path resolution in MDX files. When using absolute paths (starting with `/`) for images in static directories, the wrong file path is being returned, causing images to fail loading even when they exist in one of the configured static directories.

### Reproduction

```md
<!-- In an MDX file -->
![My Image](/img/logo.png)
```

Setup:
- Multiple static directories configured (e.g., `static`, `public`)
- Image file exists in the second static directory: `public/img/logo.png`
- First static directory (`static/img/logo.png`) does not contain the image

### Expected behavior

The loader should:
1. Check each static directory sequentially
2. Return the path where the image actually exists
3. Successfully load and process the image

### Actual behavior

The image fails to load. It appears the loader is returning the path to the first static directory regardless of whether the file actually exists there, instead of returning the path where the file was found.

This seems to have started happening recently. Images with absolute paths that worked before are now broken when they're not in the first configured static directory.

---
Repository: /testbed
