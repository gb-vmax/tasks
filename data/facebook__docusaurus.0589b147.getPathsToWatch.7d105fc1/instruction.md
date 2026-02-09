# Bug Report

### Describe the bug

After a recent update, the blog plugin is not watching content files correctly. When I create or modify blog posts, the dev server doesn't pick up the changes and I have to manually restart it.

### Reproduction

1. Start the dev server with a blog plugin configured
2. Create a new blog post in the content directory
3. The dev server doesn't detect the new file and doesn't rebuild

This seems to affect all markdown files in the blog content directories. The issue appeared after updating to the latest version.

### Expected behavior

The dev server should automatically detect changes to blog post files and trigger a rebuild without requiring a manual restart.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
