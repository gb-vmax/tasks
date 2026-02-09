# Bug Report

### Describe the bug

I'm encountering an issue with directive name parsing where names ending with hyphens or underscores are being accepted when they should be rejected. The parser is allowing invalid directive names that end with `-` or `_` characters.

### Reproduction

```markdown
:::directive-
content
:::

:::another_directive_
more content
:::
```

These directives with trailing hyphens/underscores are currently being parsed successfully, but they should be treated as invalid since directive names shouldn't end with these characters.

### Expected behavior

Directive names ending with `-` or `_` should be rejected by the parser. Only alphanumeric characters should be allowed at the end of directive names, while hyphens and underscores should only be valid in the middle of names (like `my-directive` or `my_directive`).

Valid examples:
- `:::my-directive:::`
- `:::directive_name:::`
- `:::directive123:::`

Invalid examples (should not parse):
- `:::directive-:::`
- `:::name_:::`

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
