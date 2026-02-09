# Bug Report

### Describe the bug

I'm experiencing an issue with code fence parsing in MDX where fenced code blocks are not being properly recognized. It seems like the whitespace handling at the start of closing fence sequences is broken.

### Reproduction

```mdx
# Test Document

```js
const x = 1;
```

More content here
```

When parsing this MDX content, the closing fence (```) is not being detected correctly, causing the entire rest of the document to be treated as part of the code block instead of closing it properly.

### Expected behavior

The code fence should close properly after the JavaScript code block, and "More content here" should be parsed as regular markdown content, not as part of the code block.

### Additional context

This appears to affect any fenced code blocks in MDX documents. The parser seems to have trouble with the whitespace/indentation logic when checking for closing fence sequences.

---
Repository: /testbed
