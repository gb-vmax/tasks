# Bug Report

### Describe the bug

I'm experiencing an issue where imports from markdown files are being incorrectly detected. It seems like the import detection logic is matching files that shouldn't be considered valid markdown imports.

### Reproduction

When I try to import from files with extensions like `.mdx.backup` or `.md.old`, they're being treated as valid markdown imports even though they shouldn't be.

For example:
```js
import Something from './file.mdx.backup'
import Another from './doc.md.tmp'
```

These imports are being processed as if they were regular `.md` or `.mdx` files, which causes unexpected behavior in the build process.

### Expected behavior

Only files that end with `.md` or `.mdx` (and nothing after) should be treated as markdown imports. Files like `.mdx.backup`, `.md.old`, or `.mdx.tmp` should not match the markdown import pattern.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
