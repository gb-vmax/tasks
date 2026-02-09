# Bug Report

### Describe the bug

Images with alt text are not being parsed correctly in MDX documents. When trying to use standard markdown image syntax like `![alt text](url)`, the parser fails to recognize it properly and the image doesn't render.

### Reproduction

```md
![My Image](https://example.com/image.png)
```

The above markdown should render an image but it's not being parsed correctly. The image syntax appears to be broken in the current version.

### Expected behavior

Standard markdown image syntax `![alt](url)` should be properly parsed and rendered as an image element. This is basic markdown functionality that should work out of the box.

### Additional context

This seems to have broken recently. The same syntax was working fine in previous versions. Regular links with `[text](url)` still work, but the image variant with the exclamation mark doesn't.

---
Repository: /testbed
