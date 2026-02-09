# Bug Report

### Describe the bug

I'm encountering an issue with directive containers in remark-directive where empty containers (containers with no content) are not being parsed correctly. When a directive container fence is immediately followed by EOF or a line ending without any content, the parser seems to be handling it incorrectly.

### Reproduction

```markdown
:::note
:::
```

Or with attributes:

```markdown
:::note{.info}
:::
```

When parsing these empty directive containers, the behavior is unexpected - it seems like the parser is not properly recognizing the closing fence when there's no content between the opening and closing fences.

### Expected behavior

Empty directive containers should be valid and parse correctly, creating a container node with no children. The opening fence followed immediately by a closing fence (with or without content in between) should be handled gracefully.

### Additional context

This appears to affect directive containers specifically. Other directive types (text and leaf directives) don't seem to have this issue. The problem manifests when the container has no content lines between the opening and closing fences.

---
Repository: /testbed
