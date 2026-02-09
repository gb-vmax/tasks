# Bug Report

### Describe the bug

The broken link error messages are displaying incorrect information. When a broken link is detected, the error message shows the resolved link as the main link and the original link in parentheses, which is backwards from what it should be. Additionally, the resolved link is being shown in parentheses even when it's the same as the original link.

### Reproduction

When you have a broken link in your documentation, the error message displays like this:

```
/docs/resolved-path (resolved as: /docs/original-path)
```

But it should be:

```
/docs/original-path (resolved as: /docs/resolved-path)
```

Also, when the original link and resolved link are the same, it still shows the "(resolved as: ...)" part unnecessarily.

### Expected behavior

- The error message should show the original link first, followed by the resolved link in parentheses (if different)
- When the original link and resolved link are identical, the "(resolved as: ...)" part should not be displayed
- The format should be: `original-link (resolved as: resolved-link)` only when they differ

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
