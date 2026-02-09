# Bug Report

### Describe the bug

I'm experiencing an issue where markdown imports are not being detected properly in my MDX files. It seems like the import detection logic is broken - all my markdown file imports are being ignored or not processed correctly.

### Reproduction

```js
// In an MDX file
import SomeContent from './content.md'
import AnotherDoc from './another.mdx'

// These imports are not being recognized
// The content doesn't get included/processed as expected
```

### Expected behavior

When importing `.md` or `.mdx` files using import statements, they should be properly detected and processed by the MDX loader. The imported content should be available and rendered in the document.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have broken recently - it was working fine before. Any help would be appreciated!

---
Repository: /testbed
