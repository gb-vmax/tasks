# Bug Report

### Describe the bug

I'm experiencing an issue with parsing directive labels that contain closing brackets `]`. When a directive label starts with a closing bracket, the parser doesn't handle it correctly and the bracket gets consumed improperly.

### Reproduction

```markdown
:directive[]content]
```

When parsing directives with labels that begin with `]`, the parser seems to exit the label parsing too early or handle the bracket incorrectly. The closing bracket at the start should be treated as content, but instead it's being processed in the wrong order.

### Expected behavior

Directive labels starting with `]` should be parsed correctly, with the bracket treated as part of the label content. The parser should properly track bracket balance and only close the label when encountering an unmatched closing bracket.

### Additional context

This appears to be related to how the label factory handles the initial bracket check versus setting up the token structure. The bracket balance logic seems to be evaluated at the wrong point in the parsing flow.

---
Repository: /testbed
