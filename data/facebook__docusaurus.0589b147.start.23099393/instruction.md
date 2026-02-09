# Bug Report

### Describe the bug

After a recent update, directive container parsing seems to be broken. The parser is not correctly recognizing directive containers in markdown, causing them to either not parse at all or parse incorrectly.

### Reproduction

```markdown
::: note
This is a note directive
:::
```

When processing the above markdown with remark-directive, the directive container is not being parsed correctly. The fence and sequence tokens appear to be in the wrong order during tokenization.

### Expected behavior

The directive container should be properly tokenized with the correct token structure. The parser should recognize the `:::` fence markers and properly parse the content inside as a directive container.

### Additional context

This appears to be related to the tokenization phase where directive containers are being processed. The issue manifests when trying to parse any container directive syntax (using `:::`).

---
Repository: /testbed
