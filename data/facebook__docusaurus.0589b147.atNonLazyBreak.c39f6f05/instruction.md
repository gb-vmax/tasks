# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code block parsing in MDX. It seems like the parser is not correctly handling line breaks within code blocks, causing the content to be processed in the wrong order or potentially duplicated.

### Reproduction

```mdx
# Test Document

```javascript
function example() {
  console.log('test');
  return true;
}
```

Some text after the code block.
```

When parsing this MDX content, the code block doesn't close properly and subsequent content may be incorrectly included in the code block or the parser enters an unexpected state.

### Expected behavior

The fenced code block should be properly tokenized with:
1. Opening fence detected
2. Content inside the code block processed
3. Closing fence detected
4. Content after the code block treated as separate from the code block

The parser should correctly identify line endings and transitions between code block content and the closing fence.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
