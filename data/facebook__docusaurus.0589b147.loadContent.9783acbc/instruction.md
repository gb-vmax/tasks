# Bug Report

### Describe the bug

I'm getting an error when trying to build my docs site, even though I have documentation files in my content directory. The error message says the docs version has no docs, but the files are definitely there.

### Reproduction

1. Set up a Docusaurus site with the docs plugin
2. Add some markdown files to the docs directory (e.g., `intro.md`, `tutorial.md`)
3. Run the build command
4. Get an error: `Docs version "current" has no docs! At least one doc should exist at "docs".`

This is really strange because the docs folder is not empty. I can see the files in the filesystem and they were working fine before.

### Expected behavior

The build should succeed when documentation files exist in the docs directory. The error should only appear when the directory is actually empty.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
