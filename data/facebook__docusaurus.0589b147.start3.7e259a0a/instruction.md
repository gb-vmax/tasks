# Bug Report

### Describe the bug

I'm experiencing an issue with code fence parsing in MDX where the closing fence marker is not being properly recognized when there's whitespace before it. The parser seems to be passing the wrong arguments, causing the fence to not close correctly.

### Reproduction

```mdx
    ```js
    const x = 1;
    ```
```

When there's indentation before the closing fence (``````), the code block doesn't close properly and continues consuming subsequent content as part of the code block.

### Expected behavior

The closing fence should be recognized regardless of preceding whitespace (up to the allowed indentation limit), and the code block should close correctly. The parser should handle indented closing fences the same way it handles opening fences.

### Additional context

This seems to affect code blocks with indentation, particularly when `codeIndented` is not disabled in the parser constructs. The issue appears to be related to how the sequence close detection is being called.

---
Repository: /testbed
