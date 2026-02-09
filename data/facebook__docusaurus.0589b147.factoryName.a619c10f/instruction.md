# Bug Report

### Describe the bug

I'm experiencing an issue with directive names in the remark-directive parser. When using directives that start with a number or end with a hyphen/underscore, the parser is not handling them correctly.

### Reproduction

```markdown
::1directive
This should work but doesn't parse correctly

::valid-directive-
This also fails to parse

::another_directive_
Same issue here
```

The directives starting with numbers (like `::1directive`) are being rejected when they should be accepted, and directives ending with hyphens or underscores (like `::valid-directive-` or `::another_directive_`) are being accepted when they should be rejected.

### Expected behavior

- Directive names should be allowed to start with numbers (e.g., `::1directive`)
- Directive names should NOT be allowed to end with hyphens or underscores (e.g., `::valid-directive-` should be invalid)

The current behavior seems to be the opposite of what's expected.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
