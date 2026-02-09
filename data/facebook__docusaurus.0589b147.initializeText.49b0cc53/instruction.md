# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where text content is not being processed correctly. The parser seems to be getting stuck or not properly handling data tokens when encountering certain character sequences.

### Reproduction

When trying to parse markdown content with specific character patterns, the parser either hangs indefinitely or produces incorrect output. This appears to affect basic text parsing functionality.

Example markdown that triggers the issue:
```markdown
This is a simple text with some characters that should be parsed normally.
```

The parser should handle this without any issues, but instead it seems to get into an infinite loop or skip over content that should be captured.

### Expected behavior

The markdown parser should correctly tokenize and process text data, properly entering and exiting data states as it encounters break points in the content. All text should be consumed and processed without getting stuck.

### Additional context

This seems to affect the core text initialization logic. The issue manifests when the parser tries to determine break points in the text stream and decide whether to continue in data mode or exit to handle other constructs.

---
Repository: /testbed
