# Bug Report

### Describe the bug

Markdown links are not being parsed correctly when using reference-style links. The parser appears to be checking for inactive label starts in the wrong way, causing valid reference links to be rejected.

### Reproduction

```markdown
[example]: https://example.com

This is a [reference link][example] that should work.
```

When parsing the above markdown, the reference link is not being recognized and rendered as a proper link. Instead, it's being treated as plain text.

### Expected behavior

Reference-style links should be properly parsed and converted to anchor tags. The link `[reference link][example]` should resolve to the defined reference `[example]: https://example.com` and render as a clickable link.

### Additional context

This seems to have broken recently. Regular inline links like `[text](url)` still work fine, but reference-style links are failing. The issue appears to be related to how the label end tokenizer validates whether a label start is active or not.

---
Repository: /testbed
