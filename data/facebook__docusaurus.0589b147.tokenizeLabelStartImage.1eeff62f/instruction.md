# Bug Report

### Describe the bug

Image links in markdown are not being parsed correctly. When trying to use the standard markdown image syntax `![alt text](url)`, the parser fails to recognize it properly.

### Reproduction

```js
const markdown = '![example image](https://example.com/image.png)';
// Parser fails to recognize this as an image
```

When I try to parse markdown containing image links, they're not being tokenized as expected. The opening bracket sequence `![` should trigger image parsing but it seems like the parser is looking for the wrong character code.

### Expected behavior

Standard markdown image syntax like `![alt](url)` should be parsed correctly and converted to the appropriate image nodes in the AST.

### Additional context

This appears to be related to the label marker detection in the tokenizer. Regular links with `[text](url)` might still work, but the image variant with the exclamation mark prefix is broken.

---
Repository: /testbed
