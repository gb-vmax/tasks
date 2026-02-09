# Bug Report

### Describe the bug

When setting a slug in the frontmatter that starts with `/`, the generated URL path is not working as expected. It seems like the leading slash is being handled incorrectly, causing navigation issues.

### Reproduction

Create a markdown file with the following frontmatter:

```md
---
slug: /my-custom-path
---

# My Document
```

The generated path doesn't match what I would expect based on the slug value. The behavior seems inconsistent with how absolute paths should work.

### Expected behavior

When I specify a slug starting with `/`, I expect it to create an absolute path from the docs root. The slash should be properly handled to create the correct URL structure.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
