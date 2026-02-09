# Bug Report

### Describe the bug

I'm encountering an issue with directive parsing where inline directives are not being properly terminated. It appears that directives are now accepting content that should cause them to fail parsing.

### Reproduction

```markdown
:directive[text] some extra content that shouldn't be allowed
```

The above should fail to parse as a valid directive leaf since there's content after the closing bracket, but it's being accepted instead.

Also seeing issues with directives at end of file:

```markdown
:directive[text]
```

This should parse correctly when followed by EOF, but the behavior seems off.

### Expected behavior

- Directive leaves should only be valid when followed by end of line or EOF
- Any additional content after the directive closing bracket should cause the directive to not be recognized
- The parser should properly handle both `null` (EOF) and line ending cases

### System Info
- remark-directive version: 3.0.0

---
Repository: /testbed
