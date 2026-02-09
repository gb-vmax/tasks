# Bug Report

### Describe the bug

When passing custom admonition options to the MDX loader, the configuration is being ignored and the default options are used instead. It seems like the custom options are not being applied correctly.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          remarkPlugins: [
            [require('./admonitions'), {
              tag: '!!!',
              keywords: ['custom-note', 'custom-warning']
            }]
          ]
        }
      }
    ]
  ]
}
```

When I try to use custom admonition keywords or tags, they don't work. The plugin only recognizes the default keywords (note, tip, warning, etc.) even though I've explicitly configured custom ones.

### Expected behavior

The plugin should use my custom configuration when provided. If I specify custom keywords or tags, those should be recognized instead of falling back to defaults.

### Additional context

This seems to have started recently. Previously I could customize the admonition options without issues. Now it's like the custom config is completely ignored and only the default settings are being used.

---
Repository: /testbed
