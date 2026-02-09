# Bug Report

### Describe the bug

I'm experiencing an issue with code fence parsing in markdown. When I have fenced code blocks with leading spaces (indented code fences), they're not being parsed correctly. The closing fence delimiter seems to be ignored or mishandled when there are spaces before it.

### Reproduction

```markdown
    ```js
    const x = 1;
    ```
```

When parsing this markdown with indented code fences, the closing fence is not recognized properly and the code block doesn't close as expected.

### Expected behavior

Indented fenced code blocks should be parsed correctly, with both opening and closing fence delimiters being recognized regardless of leading whitespace. The code block should properly close when the closing fence is encountered.

### Additional context

This seems to affect markdown parsing when code fences have leading spaces. The issue appears to be related to how the parser handles whitespace before fence sequences.

---
Repository: /testbed
