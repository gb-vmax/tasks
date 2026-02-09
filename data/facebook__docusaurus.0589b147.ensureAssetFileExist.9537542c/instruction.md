# Bug Report

### Describe the bug

I'm experiencing an issue where asset validation is behaving incorrectly when processing markdown links. It appears that assets that don't exist are being accepted, while valid assets might be throwing errors.

### Reproduction

```md
<!-- In a markdown file -->
![Image](./non-existent-image.png)
```

When building the site with the above markdown, the build should fail because the image doesn't exist. However, it seems like the validation logic is inverted - it's not catching missing assets properly.

### Expected behavior

The build process should throw an error with a message like "Asset ./non-existent-image.png does not exist" when referencing non-existent files. Valid assets should be processed without errors.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

This seems to have started happening recently. The error messages about missing assets aren't appearing when they should, which makes it hard to catch broken links during development.

---
Repository: /testbed
