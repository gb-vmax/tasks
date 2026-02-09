# Bug Report

### Describe the bug

I'm encountering an issue with directive name parsing in remark-directive. It appears that directive names are being consumed incorrectly - characters that should be valid in directive names are causing the parser to exit prematurely, while invalid characters are being consumed.

### Reproduction

```markdown
:valid-directive-name[content]

:another_valid_name[content]

:directive123[content]
```

When parsing the above directives, the parser seems to be rejecting valid directive names that contain hyphens, underscores, or alphanumeric characters. The behavior is inverted from what's expected.

### Expected behavior

Directive names should accept:
- Hyphens (`-`)
- Underscores (`_`) 
- Alphanumeric characters

The parser should consume these valid characters and continue parsing the directive name, only exiting when it encounters an invalid character.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

This seems like it might be a logic error in the name parsing function. The validation condition appears to be backwards.

---
Repository: /testbed
