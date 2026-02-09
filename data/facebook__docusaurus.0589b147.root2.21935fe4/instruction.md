# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with how MDX content is being processed. It seems like there's a problem with how child nodes are being handled during the compilation phase - specifically when dealing with sequences of text nodes followed by other elements.

### Reproduction

When processing MDX content that has multiple consecutive text nodes followed by non-text elements, the output structure appears incorrect. The text nodes aren't being properly grouped or flushed before the next element.

Example MDX content that triggers the issue:
```mdx
Some text here
More text
<Component />
Additional text
```

The compiled output doesn't maintain the correct structure - text nodes that should be grouped together are being separated or lost in the final output.

### Expected behavior

All consecutive text nodes should be properly collected and included in the output before moving on to the next non-text element. The structure of the original MDX should be preserved in the compiled result.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
