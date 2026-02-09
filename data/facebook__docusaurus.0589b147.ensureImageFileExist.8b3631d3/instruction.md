# Bug Report

### Describe the bug

Images that exist on the filesystem are being reported as "not found" when processing MDX files. The build fails with an error message saying the image cannot be found, even though the image file is actually present in the correct location.

### Reproduction

1. Create an MDX file with an image reference
2. Place the actual image file in the correct path
3. Build the project

Example MDX content:
```md
![My Image](./assets/image.png)
```

The image file exists at `./assets/image.png` but the build fails with:
```
Image assets/image.png used in assets/image.png not found.
```

### Expected behavior

The build should succeed when the referenced image file exists. Images that are actually present should not trigger "not found" errors.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
