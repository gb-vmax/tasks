# Bug Report

### Describe the bug

When passing custom options to the admonitions plugin, the configuration is being ignored and defaults are used instead. It seems like any custom admonition configuration I provide gets overridden by the default settings.

### Reproduction

```js
// In docusaurus.config.js
const config = {
  presets: [
    [
      'classic',
      {
        docs: {
          remarkPlugins: [
            [require('./admonitions'), {
              tag: '!!!',
              keywords: ['custom', 'mytype']
            }]
          ]
        }
      }
    ]
  ]
}
```

When I try to use custom admonition types or change the tag syntax, my options are completely ignored and the default admonition behavior is used instead.

### Expected behavior

Custom admonition options should be respected. When I provide `tag: '!!!'` or custom keywords, those should override the defaults, not be ignored.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
