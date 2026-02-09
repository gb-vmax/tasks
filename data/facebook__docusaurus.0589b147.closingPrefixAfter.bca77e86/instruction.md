# Bug Report

### Describe the bug

I'm experiencing an issue with directive container parsing where the closing fence tokens are being entered in the wrong order. This causes problems when processing markdown with container directives - the token structure becomes malformed and doesn't match the expected AST format.

### Reproduction

```markdown
::: container
Some content here
:::
```

When parsing this directive container, the closing fence sequence generates tokens in an incorrect order. The `directiveContainerSequence` token is being entered before `directiveContainerFence`, but it should be the other way around to maintain consistency with how opening fences are processed.

### Expected behavior

The closing fence should generate tokens in the same order as the opening fence:
1. First enter `directiveContainerFence`
2. Then enter `directiveContainerSequence`

This maintains the proper nesting structure and ensures the AST is correctly formed.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
