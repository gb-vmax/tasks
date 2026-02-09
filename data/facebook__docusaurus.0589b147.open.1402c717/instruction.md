# Bug Report

### Describe the bug

Image syntax in markdown is not being parsed correctly. When trying to use the standard markdown image syntax `![alt text](url)`, the parser fails to recognize it properly.

### Reproduction

```markdown
![example image](https://example.com/image.png)
```

When processing this markdown, the image syntax is not being tokenized as expected. The opening bracket sequence `![` should be followed by `[` to properly start the label, but it seems like the parser is looking for the wrong character code.

### Expected behavior

The markdown image syntax `![alt](url)` should be parsed correctly and converted to the appropriate output format. The tokenizer should properly handle the label start sequence for images.

### Additional context

This appears to affect all image references in markdown documents. Regular link syntax `[text](url)` works fine, but the image variant with the exclamation mark does not.

---
Repository: /testbed
