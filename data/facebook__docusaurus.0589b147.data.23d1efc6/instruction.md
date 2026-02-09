# Bug Report

### Describe the bug

I'm encountering an issue with the remark-directive parser where escape sequences in directive labels are not being handled correctly. When using backslashes to escape characters within directive labels, the parser seems to be calling the wrong function, which causes the escaped characters to not be processed as expected.

### Reproduction

```markdown
:directive[label with \] escaped bracket]

:directive[text with \\ backslash]
```

When parsing directives with escaped characters (like `\]` or `\\`) inside the label, the escape handling appears to be inverted - it's treating non-escape characters as if they should trigger escape processing and vice versa.

### Expected behavior

The parser should correctly handle escape sequences in directive labels:
- `\]` should be treated as a literal `]` character
- `\\` should be treated as a literal `\` character
- Other escape sequences should work as documented

The directive label parser should properly toggle between normal data processing and escape sequence handling based on whether a backslash is encountered.

### Additional context

This seems to affect the label parsing logic specifically. The issue manifests when trying to include special characters like brackets or backslashes within directive labels that need to be escaped.

---
Repository: /testbed
