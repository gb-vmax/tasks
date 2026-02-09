# Bug Report

### Describe the bug

I'm experiencing an issue with slug generation in Docusaurus docs. When I set a custom slug in the frontmatter that starts with `/`, it's not being used correctly. Instead, the slug seems to be getting processed in an unexpected way.

### Reproduction

Create a markdown file with frontmatter like this:

```md
---
slug: /custom-path
---

# My Document

Some content here.
```

The expected behavior is that the document should be accessible at `/custom-path`, but it's not working as expected. The slug handling seems to be reversed - absolute paths (starting with `/`) aren't being treated properly.

### Expected behavior

When I specify a slug starting with `/` in the frontmatter, it should be used as an absolute path for the document. This was working in previous versions but seems to have broken recently.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
