# Bug Report

### Describe the bug

I'm experiencing an issue with image syntax parsing in MDX. When using the image syntax `![alt text](url)`, the parser seems to be rejecting valid image markdown in certain cases, particularly when there's a caret character (`^`) immediately following the opening bracket.

### Reproduction

```md
![^image](test.png)
```

The above markdown should be parsed as a valid image with alt text `^image`, but it's being rejected by the parser.

Additionally, normal images without the caret seem to work fine:
```md
![normal image](test.png)  <!-- works -->
![^with caret](test.png)   <!-- doesn't work -->
```

### Expected behavior

Images with alt text starting with `^` should be parsed correctly, just like any other character. The caret character is valid in alt text and shouldn't cause the image syntax to be rejected.

### System Info
- MDX version: 3.0.0
- Parser: micromark-based

---
Repository: /testbed
