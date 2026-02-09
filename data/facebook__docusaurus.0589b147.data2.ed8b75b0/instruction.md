# Bug Report

### Describe the bug

I'm experiencing an issue with ATX heading parsing where the heading text is not being properly captured. It seems like the text content of headings is getting lost or not processed correctly during tokenization.

### Reproduction

```markdown
# This is a heading
## Another heading with text
### Heading with special characters #
```

When parsing the above markdown, the heading text appears to be incomplete or not captured properly. The heading sequence (the `#` symbols) is detected, but the actual text content seems to be affected.

### Expected behavior

The parser should correctly capture and process the full text content of ATX headings, including any characters up to the line ending or closing sequence. The text should be available in the tokenized output.

### Additional context

This appears to be related to how the `atxHeadingText` token is being exited during the parsing process. The text content should be fully consumed before the token is closed.

---
Repository: /testbed
