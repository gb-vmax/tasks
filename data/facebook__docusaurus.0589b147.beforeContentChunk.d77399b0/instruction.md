# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. When a code block is empty or contains only whitespace, it seems to cause unexpected behavior. The parser appears to be treating the code block content incorrectly.

### Reproduction

```markdown
```js
```

```

or

```markdown
```python

```
```

When parsing markdown with empty fenced code blocks like the examples above, the content is not being processed as expected. The code block should be recognized and parsed correctly even when empty.

### Expected behavior

Empty fenced code blocks should be parsed correctly and treated as valid code blocks with no content. The parser should handle the case where there's nothing between the opening and closing fence markers.

### Additional context

This seems to affect any language identifier - whether it's `js`, `python`, `ruby`, etc. The issue occurs consistently with empty code blocks across different markdown documents.

---
Repository: /testbed
