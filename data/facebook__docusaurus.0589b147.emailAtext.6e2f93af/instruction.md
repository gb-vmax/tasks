# Bug Report

### Describe the bug

Autolink email parsing is broken - emails in markdown are not being recognized correctly. When I try to use autolinks with email addresses, they're not being tokenized properly.

### Reproduction

```markdown
<user@example.com>
```

The email autolink should be parsed and converted to a proper link, but instead it's being rejected or not recognized at all.

### Expected behavior

Email autolinks should be properly parsed and recognized. The parser should:
1. Read the local part of the email (before @)
2. Recognize the @ symbol
3. Read the domain part (after @)
4. Successfully tokenize the complete email address

Currently it seems like the state transitions in the email parsing logic are incorrect, causing valid email addresses to fail parsing.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
