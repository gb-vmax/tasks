# Bug Report

### Describe the bug

I'm experiencing an issue where MDX files are being treated as Markdown files and vice versa. It seems like the file format detection logic is inverted - `.mdx` files are being processed as `md` format and `.md` files are being processed as `mdx` format.

### Reproduction

1. Create a file with `.mdx` extension containing MDX-specific syntax (e.g., JSX components)
2. The file gets processed as plain Markdown instead of MDX
3. Similarly, `.md` files are being processed as MDX when they should be treated as Markdown

For example:
- `docs/example.mdx` → incorrectly detected as `md` format
- `docs/example.md` → incorrectly detected as `mdx` format

### Expected behavior

Files should be processed according to their extension:
- `.mdx` files should be processed as MDX format
- `.md` and `.markdown` files should be processed as Markdown format

This was working correctly in previous versions but seems to have broken recently.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
