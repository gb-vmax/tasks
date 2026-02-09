# Bug Report

### Describe the bug

I'm experiencing an issue where valid image files in my MDX content are causing build errors. The build fails with an error message saying the image doesn't exist, even though the file is clearly present in the specified path.

### Reproduction

1. Create an MDX file with an image reference:
```md
![My Image](./images/screenshot.png)
```

2. Ensure the image file actually exists at `./images/screenshot.png`
3. Run the build
4. Build fails with error: `Image ./images/screenshot.png`

### Expected behavior

The build should succeed when the image file exists at the specified path. The error should only be thrown when the image file is actually missing.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems like it might be a regression - it was working fine in previous versions. The error message is backwards - it's complaining about images that DO exist rather than images that DON'T exist.

---
Repository: /testbed
