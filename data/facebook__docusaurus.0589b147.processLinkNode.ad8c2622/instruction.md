# Bug Report

### Describe the bug

Links to `.md` and `.mdx` files are not being processed correctly in MDX content. When I reference a markdown file using a relative path, the link doesn't get transformed as expected.

### Reproduction

```md
[Link to another doc](./other-doc.md)
[Link to MDX file](../guide.mdx)
```

These links should be processed and transformed, but they're being skipped entirely. Only links with `.html` extension or `@site/` alias seem to work now.

### Expected behavior

Links to `.md` and `.mdx` files should be processed and transformed just like other asset links. The transformer should recognize these as valid documentation references and handle them appropriately.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
