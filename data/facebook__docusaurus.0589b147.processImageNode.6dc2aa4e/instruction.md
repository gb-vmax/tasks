# Bug Report

### Describe the bug

Images with protocols (like `http://` or `https://`) are being incorrectly processed as local image paths, causing build failures. After a recent update, external image URLs are no longer being handled correctly and the loader is trying to resolve them as local file paths.

### Reproduction

```md
![External image](https://example.com/image.png)
```

When using an external image URL with a protocol in MDX content, the build fails because it tries to resolve the URL as a local file path instead of leaving it as-is.

### Expected behavior

External images with protocols (http://, https://, etc.) should be left unchanged and not processed through the webpack loader. Only relative/local image paths should be converted to require calls.

### Additional context

This appears to have started happening after a change to the image transformation logic. The protocol check seems to have been modified in a way that breaks handling of external URLs.

---
Repository: /testbed
