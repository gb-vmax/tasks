# Bug Report

### Describe the bug

I'm encountering an issue with directive container parsing where the token structure appears to be malformed. When using container directives (the `:::` syntax), the parser seems to be entering duplicate token states which causes unexpected behavior in the AST.

### Reproduction

```markdown
::: note
This is a container directive
:::
```

When parsing the above markdown with remark-directive, the token structure for `directiveContainerFence` gets duplicated in the entry sequence, leading to an incorrect AST representation.

### Expected behavior

The parser should properly enter the token states in the correct order without duplication:
1. `directiveContainer`
2. `directiveContainerFence` 
3. `directiveContainerSequence`

Instead, it appears to be entering `directiveContainerFence` twice which breaks the expected token hierarchy.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

This seems to affect all container directives regardless of the directive name or content. Any help would be appreciated!

---
Repository: /testbed
