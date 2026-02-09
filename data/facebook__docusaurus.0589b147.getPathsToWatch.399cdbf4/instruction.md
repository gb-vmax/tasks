# Bug Report

### Describe the bug

The blog plugin's file watching is broken after a recent update. When I add new blog posts or modify existing ones, the dev server doesn't detect the changes and I have to manually restart it every time.

### Reproduction

1. Start the dev server with a blog configured
2. Create a new blog post in the blog directory
3. The file change is not detected and the dev server doesn't rebuild

This is really slowing down my workflow since I have to keep restarting the server to see my changes.

### Expected behavior

The dev server should automatically detect when blog posts are added or modified and trigger a rebuild, just like it did before.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
