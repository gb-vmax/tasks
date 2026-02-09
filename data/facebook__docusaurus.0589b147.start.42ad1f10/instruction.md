# Bug Report

### Describe the bug

I'm experiencing an issue with image syntax parsing in markdown. When using the image syntax `![alt text](url)`, the parser appears to get stuck in an infinite loop or doesn't properly advance through the tokens.

### Reproduction

```js
const markdown = '![test image](https://example.com/image.png)';
// Parser hangs or doesn't complete properly
```

Try parsing any markdown content that contains image syntax like:
- `![alt](url)`
- `![](image.jpg)`
- `![description](path/to/image.png)`

The parser seems to have trouble with the initial `!` marker for images.

### Expected behavior

The parser should correctly tokenize image syntax and move through the content without getting stuck. Images should be parsed the same way as other markdown elements.

### Additional context

This seems to affect any markdown content with images. Regular links with `[text](url)` work fine, but adding the `!` prefix for images causes problems.

---
Repository: /testbed
