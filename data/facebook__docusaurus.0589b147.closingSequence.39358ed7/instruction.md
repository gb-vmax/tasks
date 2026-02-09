# Bug Report

### Describe the bug

I'm experiencing an issue with directive container parsing where the closing fence sequence is not being validated correctly. When using directive containers (like `:::container`), the parser seems to be accepting closing sequences that don't match the opening sequence length.

### Reproduction

```markdown
:::note
Some content here
::
```

The above should NOT be valid since the closing sequence `::` (2 colons) doesn't match the opening sequence `:::` (3 colons). However, it appears to be parsed as a valid container.

Similarly:

```markdown
::::warning
Content
:::
::::
```

The first closing sequence `:::` should be ignored (treated as content) since it has fewer colons than the opening `::::`, but it seems like the parser is incorrectly treating it as the closing fence.

### Expected behavior

The parser should only accept a closing fence that has **at least** the same number of colons as the opening fence. Closing fences with fewer colons should be treated as regular content inside the container, not as the closing delimiter.

For example:
- `:::container` should only close with `:::` or more colons
- `::::container` should only close with `::::` or more colons
- A closing sequence with fewer colons should remain as content

This is consistent with how other fence-based syntax works in markdown (like code blocks with backticks).

---
Repository: /testbed
