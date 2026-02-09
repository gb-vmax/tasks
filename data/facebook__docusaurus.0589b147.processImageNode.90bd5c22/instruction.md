# Bug Report

### Describe the bug

Images with protocols (like `http://`, `https://`, etc.) are being incorrectly processed and converted to require calls instead of being left as-is. This causes build failures when using external image URLs in MDX files.

### Reproduction

```mdx
<!-- This should work but fails after recent changes -->
![External Image](https://example.com/image.png)

<!-- This also fails -->
![Protocol Image](http://example.com/photo.jpg)
```

When building the site, these external image URLs are being treated as local paths and webpack tries to resolve them, which obviously fails since they're remote URLs.

### Expected behavior

Images with protocols (http://, https://, etc.) should be left unchanged and not processed through webpack's require system. Only relative/local image paths without protocols should be converted to require calls.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have started happening recently. External images used to work fine before.

---
Repository: /testbed
