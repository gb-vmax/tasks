# Bug Report

### Describe the bug

Autolink email parsing is broken - emails with `@` symbols are not being recognized correctly. The parser seems to be rejecting valid email addresses in autolink syntax.

### Reproduction

```markdown
<user@example.com>
<test@domain.org>
```

When parsing markdown with autolink email addresses, the parser fails to recognize them as valid autolinks. The `@` symbol appears to be causing the tokenizer to reject the input prematurely.

### Expected behavior

Email autolinks should be parsed correctly and converted to proper link nodes. The format `<email@domain.com>` should be recognized as a valid autolink.

### Additional context

This seems to affect any email autolink that contains the `@` character. Regular URL autolinks like `<https://example.com>` still work fine, but email-specific autolinks are failing.

---
Repository: /testbed
