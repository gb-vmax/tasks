# Bug Report

### Describe the bug

I'm experiencing an issue with directive container parsing in remark-directive. When parsing container directives with attributes, the parser seems to get stuck or behaves incorrectly after processing the attributes section.

### Reproduction

```markdown
:::note{#custom-id .my-class}
Some content here
:::
```

When trying to parse a container directive that includes attributes (the `{#custom-id .my-class}` part), the parser doesn't handle the whitespace correctly after the attributes. The content inside the directive either doesn't get parsed properly or the parser enters an unexpected state.

This also happens with simpler cases:

```markdown
:::warning{.alert}
Warning message
:::
```

### Expected behavior

Container directives with attributes should be parsed correctly, and the content inside them should be processed as expected. The whitespace after the attributes block should be handled properly before moving to the next parsing stage.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
