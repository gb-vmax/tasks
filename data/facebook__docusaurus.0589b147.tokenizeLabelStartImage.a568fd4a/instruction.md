# Bug Report

### Describe the bug

I'm experiencing an issue with image syntax parsing in MDX. It seems like the image label tokenizer is incorrectly handling certain edge cases, causing valid image syntax to be rejected or invalid syntax to be accepted.

### Reproduction

```mdx
![alt text](image.png)
```

When processing MDX content with image references, the parser behaves unexpectedly. Images that should be valid are not being recognized properly, or conversely, malformed image syntax is being accepted when it shouldn't be.

This appears to be related to how the label image tokenizer handles character codes during parsing, particularly around the validation logic.

### Expected behavior

The MDX parser should correctly identify and process image syntax according to the CommonMark/MDX specification. Valid image references should be parsed successfully, and invalid ones should be rejected.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
