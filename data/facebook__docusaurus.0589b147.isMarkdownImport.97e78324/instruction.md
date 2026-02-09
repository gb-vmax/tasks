# Bug Report

### Describe the bug

I'm experiencing an issue where markdown imports are not being recognized correctly in my MDX files. When I try to import `.md` or `.mdx` files, they're not being processed as expected and the table of contents generation seems to be broken.

### Reproduction

```js
// In an MDX file
import Content from './other-doc.md'
import AnotherDoc from './another.mdx'

// These imports are not being detected as markdown imports
// TOC generation fails silently
```

### Expected behavior

When importing `.md` or `.mdx` files, they should be properly recognized as markdown imports and processed accordingly. The table of contents should be generated correctly for these imported markdown files.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have started happening recently. The imports work in some cases but fail in others, making it hard to pinpoint the exact issue. Any help would be appreciated!

---
Repository: /testbed
