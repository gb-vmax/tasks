# Bug Report

### Describe the bug

I'm encountering an issue with autolink parsing where certain email addresses are not being recognized correctly. It seems like the parser is failing to properly handle email addresses that contain dots (`.`) in the local part.

### Reproduction

```markdown
<test.user@example.com>
```

When parsing the above autolink, the email address is not being recognized as valid, even though it should be according to the autolink specification.

Also noticed that some autolinks might not be returning values properly - the parser seems to be consuming characters but not completing the parsing flow correctly.

### Expected behavior

Email addresses with dots in the local part (before the `@` symbol) should be recognized as valid autolinks and parsed correctly. For example:
- `<test.user@example.com>` should be parsed as a valid email autolink
- `<first.last@domain.com>` should be parsed as a valid email autolink

### System Info
- remark version: 15.0.1

---
Repository: /testbed
