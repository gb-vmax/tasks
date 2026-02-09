# Bug Report

### Describe the bug

When using images in MDX files, I'm getting an error saying the image is not found even though the image file actually exists in the correct location. The error message appears to be backwards - it's throwing an error when the image EXISTS instead of when it's missing.

### Reproduction

1. Create an MDX file with an image reference
2. Make sure the image file actually exists at the specified path
3. Build the project

```md
![My Image](./assets/my-image.png)
```

The build fails with an error like:
```
Image docs/my-file.mdx used in assets/my-image.png not found.
```

### Expected behavior

The build should succeed when the image file exists. The error should only be thrown when the image is actually missing. Also, the error message seems to have the file paths swapped - it should say which image is missing and which source file is trying to use it, not the other way around.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
