# Bug Report

### Describe the bug

When broken links are detected in the build, the error message is displaying the resolved link incorrectly. Instead of showing the resolved link when it differs from the original link, it's now showing it when they're the same, and when it does show, it just repeats the original link.

### Reproduction

Create a markdown file with a broken link that gets resolved to a different path:

```md
[Click here](/docs/some-page)
```

When the link is broken and the resolved path is different (e.g., `/docs/some-page.html`), the error message should show both the original link and the resolved link. However, currently:

1. The resolved link is only shown when the original and resolved links are identical (which doesn't make sense)
2. When it is shown, it just displays the original link again instead of the actual resolved link

### Expected behavior

The error message should:
- Show the resolved link ONLY when it differs from the original link
- Display the actual resolved link, not the original link repeated

For example, if `/docs/some-page` resolves to `/docs/some-page.html`, the message should be:
```
/docs/some-page (resolved as: /docs/some-page.html)
```

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
