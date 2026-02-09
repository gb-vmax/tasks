# Bug Report

### Describe the bug

I'm experiencing an issue with MDX file format detection in the loader. Files with `.md` extensions are being incorrectly processed as MDX format, and files with `.mdx` extensions are being processed as Markdown format. This seems to be the opposite of what should happen.

### Reproduction

Create two files:
1. `example.md` - a standard Markdown file
2. `example.mdx` - an MDX file with JSX components

When the loader processes these files:
- `example.md` gets treated as MDX format (should be MD)
- `example.mdx` gets treated as MD format (should be MDX)

This causes parsing errors when trying to use MDX-specific features in `.mdx` files, and unnecessary MDX processing overhead for plain `.md` files.

### Expected behavior

Files should be processed according to their extension:
- `.md` files → MD format
- `.mdx` files → MDX format
- Unknown extensions → default to MDX format (as before)

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
