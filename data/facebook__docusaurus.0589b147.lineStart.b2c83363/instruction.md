# Bug Report

### Describe the bug

I'm experiencing an issue with directive container parsing where the content is not being processed correctly. It seems like the parser is terminating prematurely when it encounters content inside directive containers.

### Reproduction

```markdown
:::note
This is some content inside a directive container.
It should be parsed correctly.
:::
```

When parsing the above markdown with directive containers, the content inside the container is not being recognized properly. The parser appears to be handling the opening fence but then immediately treating the content as if it should close the container.

### Expected behavior

The parser should:
1. Recognize the opening fence `:::note`
2. Parse all content lines until it encounters the closing fence `:::`
3. Properly tokenize the content between the fences

Instead, it seems to be inverting the logic for when to continue parsing vs when to close the container.

### Additional context

This affects all directive containers (note, warning, tip, etc.) and makes them essentially unusable. The content that should be inside the container is either being ignored or parsed as if the container was already closed.

---
Repository: /testbed
