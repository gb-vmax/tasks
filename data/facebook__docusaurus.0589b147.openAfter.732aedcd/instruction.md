# Bug Report

### Describe the bug

When using directive containers in markdown, the parser doesn't handle end-of-file (EOF) conditions correctly. If a directive container fence is immediately followed by EOF without a newline, the parser fails to properly recognize and close the container.

### Reproduction

```markdown
:::note
This is a note
:::
```

When the above markdown ends without a trailing newline (i.e., the closing `:::` is at EOF), the directive container is not parsed correctly.

### Expected behavior

The directive container should be properly recognized and closed even when the closing fence is at EOF without a trailing newline. The parser should handle both cases:
- Directive container with trailing newline after closing fence
- Directive container at EOF without trailing newline

### Additional context

This seems to affect how the tokenizer handles null codes (EOF) in the `openAfter` function. The current behavior causes the parser to reject valid directive containers that happen to be at the end of a file.

---
Repository: /testbed
