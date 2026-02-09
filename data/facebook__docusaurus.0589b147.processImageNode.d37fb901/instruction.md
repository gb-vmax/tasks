# Bug Report

### Describe the bug

Images with absolute URLs (like `http://` or `https://`) are being incorrectly processed as local file paths, causing build failures. The image transformation logic seems to be treating external URLs as if they should be converted to webpack require calls.

### Reproduction

In an MDX file, try using an image with an absolute URL:

```md
![External image](https://example.com/image.png)
```

or

```md
![HTTP image](http://cdn.example.com/logo.svg)
```

### Expected behavior

External images with protocols (http://, https://, etc.) should be left as-is and not processed through webpack's require calls. Only local/relative image paths should be transformed.

### Additional context

This seems to have broken recently. Previously, images with protocols were correctly skipped during the transformation process, but now they're being treated as local paths which causes the build to fail when trying to resolve them as file paths.

---
Repository: /testbed
