# Bug Report

### Describe the bug

I'm experiencing an issue with slug generation in Docusaurus docs. When I set a frontmatter slug that starts with a single `/`, it's not being treated as an absolute path anymore. Instead, it seems to be getting concatenated with the directory structure.

### Reproduction

Create a markdown file with the following frontmatter:

```md
---
slug: /my-custom-path
---

# My Document
```

The slug is not being used as an absolute path. It appears to be getting combined with the directory name or ignored entirely.

### Expected behavior

When a slug starts with `/`, it should be treated as an absolute path from the docs root, overriding any directory-based slug generation. This was working in previous versions.

For example:
- File located at: `docs/guides/tutorial.md`
- Frontmatter: `slug: /my-custom-path`
- Expected URL: `/docs/my-custom-path`
- Actual behavior: Not using the absolute path correctly

This seems like a regression as absolute slugs with leading `/` were working before.

---
Repository: /testbed
