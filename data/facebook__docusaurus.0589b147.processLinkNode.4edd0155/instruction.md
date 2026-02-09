# Bug Report

### Describe the bug

Links with protocols (like `http://`, `https://`, etc.) are not being processed correctly in MDX files. External links that should be left as-is are being transformed, while internal markdown/HTML links that should be processed are being skipped.

### Reproduction

```md
# Example MDX file

[External link](https://example.com/page.html)
[Internal markdown link](./docs/intro.md)
[Asset link](@site/static/img/logo.png)
```

After processing:
- External links with protocols are incorrectly transformed instead of being left alone
- Internal `.md` and `.html` links without protocols are not being processed when they should be

### Expected behavior

- Links with protocols (http://, https://, etc.) should be left as-is and not transformed
- Internal links to `.md`, `.mdx`, and `.html` files without protocols should be processed normally
- Links with `@site/` alias should continue to work as expected

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
