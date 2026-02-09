# Bug Report

### Describe the bug

I'm experiencing an issue with image reference syntax in markdown parsing. When using the `![` syntax to create image references, the parser seems to be handling the tokens incorrectly, causing the image markers to not be properly recognized or processed.

### Reproduction

```markdown
![alt text][image-ref]

[image-ref]: /path/to/image.png
```

When parsing markdown with image reference syntax like above, the label markers aren't being handled correctly. The parser appears to be consuming tokens in the wrong order, which breaks the proper recognition of image references.

### Expected behavior

The parser should correctly tokenize and recognize image reference syntax (`![...]`) and properly match it with the corresponding reference definition. The label markers should be entered, consumed, and exited in the correct sequence to maintain proper token structure.

### Additional context

This seems to affect specifically the `![` image label start token processing. Regular link references with `[` appear to work fine, but the image variant with `!` prefix is having issues with how it handles the opening bracket marker.

---
Repository: /testbed
