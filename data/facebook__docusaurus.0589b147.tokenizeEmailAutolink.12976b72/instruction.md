# Bug Report

### Describe the bug

Email autolinks are no longer being recognized or parsed correctly. When markdown text contains email addresses, they should be automatically converted to clickable links, but this functionality appears to be broken.

### Reproduction

```markdown
Contact me at user@example.com for more info.

You can also reach support@company.org
```

Expected: Email addresses should be parsed as autolinks
Actual: Email addresses are treated as plain text and not converted to links

### Steps to reproduce
1. Create markdown content with an email address (e.g., `test@domain.com`)
2. Process the markdown through the parser
3. Email addresses are not converted to autolinks

This was working in previous versions but seems to have stopped working recently. WWW autolinks (like www.example.com) still work fine, but email autolinks specifically are affected.

### Expected behavior
Email addresses in markdown text should be automatically detected and converted to `mailto:` links, similar to how GitHub handles them in comments and issues.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

---
Repository: /testbed
