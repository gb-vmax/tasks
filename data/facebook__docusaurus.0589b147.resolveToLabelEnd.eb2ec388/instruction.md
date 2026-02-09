# Bug Report

### Describe the bug

I'm encountering an issue with label text parsing in MDX content. When using labels with media elements, the text boundaries seem to be calculated incorrectly, causing parts of the label text to be cut off or missing.

### Reproduction

```mdx
![alt text](image.png)

[link text](url)
```

When parsing MDX content with image or link labels, the label text doesn't get extracted correctly. The start and end positions appear to be off by one, which results in incomplete text content being captured.

### Expected behavior

The full label text should be properly extracted and parsed. For example, in `![alt text](image.png)`, the entire "alt text" string should be captured as the label text, and similarly for link labels.

### Additional context

This seems to affect how the parser resolves label boundaries when processing events. The text extraction is cutting off characters at the boundaries, making it impossible to get the complete label content.

---
Repository: /testbed
