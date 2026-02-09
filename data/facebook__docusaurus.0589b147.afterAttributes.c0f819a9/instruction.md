# Bug Report

### Describe the bug
I'm experiencing an issue with directive containers in remark-directive where whitespace handling appears to be broken. When parsing directive containers with attributes, the parser seems to be consuming whitespace incorrectly, which causes parsing failures or unexpected behavior.

### Reproduction
```markdown
:::note{#my-id .my-class}
Some content here
:::
```

When parsing directive containers that have attributes followed by content, the whitespace between the attributes and the content block is not being handled properly. This affects how the directive container is parsed and can lead to incorrect AST generation.

### Expected behavior
The parser should correctly handle whitespace after directive container attributes and properly tokenize the opening fence before moving to the content. The directive container should be parsed successfully regardless of whitespace configuration.

### System Info
- remark-directive version: 3.0.0
- Using with Jest vendor bundle

This seems to have started happening recently and is affecting markdown parsing in our documentation system. Any help would be appreciated!

---
Repository: /testbed
