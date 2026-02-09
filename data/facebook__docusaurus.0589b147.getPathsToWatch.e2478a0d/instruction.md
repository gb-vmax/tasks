# Bug Report

### Describe the bug

When using multiple content paths in the docs plugin configuration, the file watcher only monitors the first content path. Changes to files in additional content paths (2nd, 3rd, etc.) are not detected, and hot reload doesn't work for those directories.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          path: 'docs',
          // Multiple content paths configured
          include: ['**/*.md', '**/*.mdx'],
        },
      },
    ],
  ],
};
```

With a docs plugin configured to use multiple content directories:
1. Set up multiple content paths for documentation
2. Start the dev server
3. Edit a file in the second or third content path
4. The changes are not picked up by the file watcher
5. Only files in the first content path trigger hot reload

### Expected behavior

All configured content paths should be watched for changes, and modifications to any file in any of the content directories should trigger hot reload during development.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
