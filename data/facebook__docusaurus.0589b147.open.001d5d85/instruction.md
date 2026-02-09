# Bug Report

### Describe the bug

I'm encountering an issue with image link syntax parsing in MDX. When trying to use the standard markdown image syntax `![alt text](url)`, the parser seems to be failing to recognize it correctly.

### Reproduction

```markdown
![Example Image](https://example.com/image.png)
```

When I try to parse this, it doesn't work as expected. The image syntax should be recognized with the opening `![` bracket, but something seems off with how the parser is handling the bracket characters.

### Expected behavior

The parser should correctly recognize and process the image link syntax `![...]` and parse it into the appropriate AST nodes. The opening marker `![` should be properly tokenized as a label image marker.

### Additional context

This seems to be related to the label tokenization logic. The issue appears when the parser encounters the opening bracket sequence for images. It's like the parser is looking for the wrong character code after the `!` marker.

---
Repository: /testbed
