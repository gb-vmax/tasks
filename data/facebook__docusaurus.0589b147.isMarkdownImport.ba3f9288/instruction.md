# Bug Report

### Describe the bug

I'm experiencing an issue with MDX imports in my Docusaurus project. After updating, markdown/MDX file imports are no longer being recognized correctly. The table of contents generation seems to be broken when importing from other MDX files.

### Reproduction

```js
// In my MDX file
import MyComponent from './other-file.mdx'
import AnotherDoc from '../docs/guide.md'

// These imports are not being processed correctly
```

When I try to use these imports, they don't work as expected. It seems like the loader is not detecting these as markdown imports anymore.

### Expected behavior

Importing `.md` and `.mdx` files should work correctly and be recognized by the MDX loader. The TOC generation should properly handle these imports.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

Has anyone else run into this? This was working fine in the previous version.

---
Repository: /testbed
