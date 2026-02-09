# Bug Report

### Describe the bug

I'm experiencing an issue with image link parsing in MDX where the markdown syntax for images is not being recognized correctly. When I try to use standard markdown image syntax `![alt text](url)`, the parser doesn't seem to handle it properly.

### Reproduction

```markdown
![Example Image](https://example.com/image.png)
```

When parsing the above markdown, the image syntax isn't being processed as expected. It appears the tokenizer is having trouble with the label marker sequence.

### Expected behavior

The markdown image syntax should be parsed correctly and converted to the appropriate image element. The `![` sequence should be recognized as the start of an image label.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

Has anyone else encountered this? It seems like the label marker handling might have changed recently.

---
Repository: /testbed
