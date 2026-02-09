# Bug Report

### Describe the bug

I'm experiencing a syntax error in the blog plugin after a recent update. The plugin fails to load and breaks the entire build process. It looks like the code got cut off or corrupted somehow.

### Reproduction

1. Set up a Docusaurus site with the blog plugin enabled
2. Try to build or start the dev server
3. The build fails with a syntax error

The error occurs when the plugin tries to load blog content. The `loadContent()` function appears to be incomplete - it references a variable `listedBlogPost` (singular) instead of `listedBlogPosts` (plural), and the entire function body seems to be truncated.

### Expected behavior

The blog plugin should load content successfully and the site should build without errors. The `loadContent()` function should complete its execution and return the blog metadata properly.

### System Info
- Docusaurus version: Latest
- Node version: 18.x
- Package: @docusaurus/plugin-content-blog

---
Repository: /testbed
