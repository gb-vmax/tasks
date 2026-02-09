# Bug Report

### Describe the bug

The MDX loader is incorrectly determining the format for files with `.md` extensions. Files that should be treated as Markdown are being processed as MDX instead, and vice versa.

### Reproduction

When loading a file with a `.md` extension:
```js
// File: example.md
const filepath = '/path/to/example.md';
// Expected format: 'md'
// Actual format: 'mdx'
```

When loading a file with `.mdx` or other extensions:
```js
// File: example.mdx
const filepath = '/path/to/example.mdx';
// Expected format: 'mdx'
// Actual format: 'md'
```

The format detection logic appears to be inverted - `.md` files are being treated as MDX and `.mdx` files are being treated as plain Markdown.

### Expected behavior

- Files with `.md` extension should be processed with format `'md'`
- Files with `.mdx` extension (or unknown extensions) should be processed with format `'mdx'`

### System Info
- Package: @docusaurus/mdx-loader
- Affected module: packages/docusaurus-mdx-loader/src/format.ts

---
Repository: /testbed
