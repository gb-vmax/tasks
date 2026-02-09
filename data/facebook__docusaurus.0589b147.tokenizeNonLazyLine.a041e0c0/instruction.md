# Bug Report

### Describe the bug

I'm experiencing an issue with the remark-directive parser where lazy continuation lines are being handled incorrectly. It seems like the logic for determining whether a line should be treated as lazy or not has been inverted, causing directives with multi-line content to fail parsing unexpectedly.

### Reproduction

```markdown
:::note
This is a note directive
with multiple lines
that should continue
:::
```

When parsing the above markdown with remark-directive, the continuation lines are not being processed correctly. The parser appears to be rejecting valid continuation lines or accepting lines that should be rejected.

### Expected behavior

Multi-line directive content should be parsed correctly, with lazy continuation lines handled according to the CommonMark spec. The parser should properly distinguish between valid continuation lines and lines that break out of the directive context.

### Additional context

This affects any directive that spans multiple lines, including container directives like `:::note` and leaf directives with multi-line content. The issue seems to be in the tokenization logic for non-lazy lines.

---
Repository: /testbed
