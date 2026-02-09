# Bug Report

### Describe the bug

Links in MDX files are not being transformed/processed correctly. The plugin seems to be ignoring regular markdown links and only processing images instead.

### Reproduction

Create an MDX file with regular markdown links:

```md
# My Document

Check out [this link](./other-page.md) for more info.

Also see [external link](https://example.com).
```

The links are not being transformed as expected. They should be processed by the link transformer but appear to be skipped entirely.

### Expected behavior

All markdown links should be processed and transformed by the remark plugin. For example, relative links like `./other-page.md` should be resolved to the correct paths.

### System Info
- Docusaurus version: latest
- MDX loader: @docusaurus/mdx-loader

---
Repository: /testbed
