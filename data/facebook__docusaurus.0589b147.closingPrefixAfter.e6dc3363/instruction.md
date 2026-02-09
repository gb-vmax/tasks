# Bug Report

### Describe the bug

I'm encountering an issue with directive container parsing where the closing fence tokens are being entered in the wrong order. This causes problems when processing directive containers with closing fences.

### Reproduction

```markdown
::: note
Some content here
:::
```

When parsing a directive container like the one above, the closing fence (`:::`) isn't being processed correctly. The token order appears to be incorrect - `directiveContainerSequence` is being entered before `directiveContainerFence` instead of after.

### Expected behavior

The parser should enter the `directiveContainerFence` token first, then the `directiveContainerSequence` token when processing the closing fence of a directive container. The current behavior has these reversed.

Additionally, the `closingSequence` function is being called with the wrong argument - it's receiving `effects2` instead of `code`.

### Additional context

This affects any markdown content that uses directive containers with proper closing fences. The parsing tree structure ends up malformed which can break downstream processors that rely on the correct token order.

---
Repository: /testbed
