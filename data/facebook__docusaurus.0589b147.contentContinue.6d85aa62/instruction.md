# Bug Report

### Describe the bug

I'm encountering an issue with directive containers in markdown parsing. When using container directives (like `:::` syntax), the parser seems to be incorrectly handling lazy continuation lines within the directive content. This causes unexpected behavior where content that should be part of the directive is being treated differently than expected.

### Reproduction

```markdown
:::note
This is a directive container
with multiple lines of content
that should all be part of the container
:::
```

When parsing this markdown, the lazy line handling appears to be broken. The content lines within the directive container are not being processed correctly, particularly when there are multiple lines or when checking for line endings.

### Expected behavior

All content between the opening `:::note` and closing `:::` should be properly recognized as part of the directive container, with lazy continuation lines handled appropriately. The parser should correctly identify which lines belong to the directive and process them accordingly.

### Additional context

This seems related to how the parser determines lazy vs non-lazy lines within directive containers. The issue manifests when the directive contains multi-line content.

---
Repository: /testbed
