# Bug Report

### Describe the bug

I've encountered an issue with fenced code blocks in MDX. When parsing code blocks, the closing fence doesn't seem to be properly recognized, causing the parser to treat content after the code block as part of the code block itself instead of continuing with normal content parsing.

### Reproduction

```mdx
# My Document

```js
const example = 'code';
```

This text should be outside the code block but gets included in it.
```

### Expected behavior

The parser should correctly identify the closing fence (the second set of backticks) and treat any content after it as regular markdown/MDX content, not as part of the code block.

### Additional context

This appears to affect the tokenization logic for fenced code blocks. The content after a properly closed code block is being incorrectly parsed as if the code block never closed.

---
Repository: /testbed
