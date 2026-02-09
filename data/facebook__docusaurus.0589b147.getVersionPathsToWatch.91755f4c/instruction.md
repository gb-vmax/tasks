# Bug Report

### Describe the bug

After a recent update, the docs plugin is not watching all content paths correctly. When I have multiple content directories configured (like versioned docs or localized content), file changes in some directories are not triggering hot reload.

### Reproduction

Set up a docs plugin with multiple content paths:

```js
// docusaurus.config.js
{
  docs: {
    path: 'docs',
    // Multiple content paths scenario
  }
}
```

Steps to reproduce:
1. Configure docs with multiple content directories
2. Make changes to a markdown file in the second content directory
3. The dev server doesn't pick up the changes and doesn't trigger a rebuild

### Expected behavior

All configured content paths should be watched for changes, not just the first one. When I edit any markdown file in any of the configured content directories, the dev server should detect the change and hot reload.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

This seems to have started happening recently. Previously all my content directories were being watched properly.

---
Repository: /testbed
