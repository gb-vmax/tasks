# Bug Report

### Describe the bug
Image syntax in MDX is not being parsed correctly. When trying to use standard markdown image syntax `![alt text](url)`, the parser fails to recognize it properly.

### Reproduction
```mdx
![Example Image](https://example.com/image.png)
```

The image markdown should be parsed and rendered, but instead it seems like the label marker detection is inverted - it's rejecting the opening bracket `[` when it should be accepting it.

### Expected behavior
Standard markdown image syntax `![alt](url)` should be parsed correctly and the image should render in the output.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This appears to be a regression as image syntax was working in previous versions. The tokenizer seems to have an issue with the label start detection for images.

---
Repository: /testbed
