# Bug Report

### Describe the bug

I'm experiencing an issue with emphasis/attention markers in MDX content. It seems like bold text (using `**`) is not being parsed correctly - the opening and closing markers are getting confused, causing the text to render incorrectly.

### Reproduction

```mdx
This is **bold text** that should work.
```

When I render this, the bold formatting doesn't apply as expected. The markers seem to be incorrectly classified as opening vs closing delimiters.

### Expected behavior

The text between `**` markers should be rendered as bold. The tokenizer should correctly identify which markers are opening delimiters and which are closing delimiters based on the surrounding characters.

### Additional context

This appears to be related to how the attention sequence tokenizer classifies characters around the markers. The logic for determining whether a marker opens or closes an emphasis span seems off - particularly for the asterisk (`*`) marker case.

---
Repository: /testbed
