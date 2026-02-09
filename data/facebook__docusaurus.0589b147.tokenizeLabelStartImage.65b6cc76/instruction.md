# Bug Report

### Describe the bug

I'm experiencing an issue with markdown image syntax parsing. When trying to use standard markdown image syntax like `![alt text](url)`, it's not being recognized correctly. The parser seems to be rejecting valid image syntax.

### Reproduction

```markdown
![Example Image](https://example.com/image.png)
```

When I try to parse this markdown, the image syntax is not being processed as expected. It appears the opening bracket sequence for images (`![`) is not being matched properly.

### Expected behavior

The markdown parser should correctly recognize and process standard image syntax `![alt](url)`. The opening `![` should be tokenized as a valid label start for an image.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
