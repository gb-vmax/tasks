# Bug Report

### Describe the bug

After a recent update, the blog plugin is not watching markdown files correctly. When I create or modify blog posts, the dev server doesn't detect the changes and I have to manually restart it to see updates.

### Reproduction

1. Start the dev server
2. Create a new blog post or modify an existing one in the blog content directory
3. The changes are not picked up by the watcher
4. Have to restart the dev server to see the changes

### Expected behavior

The dev server should automatically detect changes to blog markdown files and trigger a hot reload without needing to restart.

### System Info
- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

This is really slowing down my workflow. Any help would be appreciated!

---
Repository: /testbed
