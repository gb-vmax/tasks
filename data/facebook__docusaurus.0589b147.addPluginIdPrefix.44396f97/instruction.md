# Bug Report

### Describe the bug

I'm experiencing an issue with the docs plugin where versioned documentation files are being generated with incorrect naming conventions when using a custom plugin ID. The plugin appears to be adding prefixes to version directories even when it shouldn't, and the separator character seems wrong.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'community',
        path: 'community',
        routeBasePath: 'community',
      },
    ],
  ],
};
```

After setting up a docs instance with a custom plugin ID like `'community'`, the versioned docs directory structure is created incorrectly. Expected the default plugin instance to have no prefix, but instead it's getting prefixed. Also noticed the separator character between plugin ID and directory name appears to be inconsistent.

### Expected behavior

- Default plugin instance (with `DEFAULT_PLUGIN_ID`) should NOT have any prefix added to version directories
- Custom plugin instances should have their plugin ID prefixed to version directories
- The separator should be consistent (underscore `_` throughout)

For example:
- Default instance: `versioned_docs/version-1.0.0`
- Custom instance with id `'community'`: `community_versioned_docs/version-1.0.0`

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
