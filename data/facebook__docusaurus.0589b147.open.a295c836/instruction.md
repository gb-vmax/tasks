# Bug Report

### Describe the bug

I'm encountering an issue with image label parsing in markdown. When using the image syntax `![alt text][ref]`, the parser seems to be behaving incorrectly and not properly handling the label markers.

### Reproduction

```markdown
![example image][image-ref]

[image-ref]: https://example.com/image.png
```

When parsing this markdown, the image reference syntax doesn't seem to be processed correctly. The label marker exit event appears to be missing, which causes issues with the token stream.

### Expected behavior

The parser should correctly tokenize image labels with proper entry and exit events for all markers. The token structure should be complete and balanced for image reference syntax.

### Additional context

This appears to affect the `tokenizeLabelStartImage` function specifically. The label marker tokens aren't being properly closed before exiting the label image context.

---
Repository: /testbed
