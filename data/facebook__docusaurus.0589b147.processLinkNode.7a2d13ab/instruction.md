# Bug Report

### Describe the bug

Links with `@site/` alias are not being processed correctly in MDX files. When I use a link like `[@site/static/img/logo.png](@site/static/img/logo.png)`, it's not being transformed as expected.

### Reproduction

Create an MDX file with the following content:

```md
Here's a link to an image: [@site/static/img/logo.png](@site/static/img/logo.png)

And here's a regular markdown link: [docs](/docs/intro.md)
```

The `@site/` prefixed link should be processed and transformed to the correct path, but it appears to be skipped entirely.

### Expected behavior

Links using the `@site/` alias should be properly transformed to their absolute paths, regardless of whether they have asset-like extensions or not. The current behavior seems to skip processing these links when they should be handled.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
