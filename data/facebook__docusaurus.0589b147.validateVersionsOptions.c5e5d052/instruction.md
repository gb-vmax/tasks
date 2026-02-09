# Bug Report

### Describe the bug

I'm encountering an issue with the `lastVersion` validation in the docs plugin. When I specify a valid version name in the `lastVersion` option, I'm getting an error saying it's invalid, even though the version exists in my versions list.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          lastVersion: '2.0.0',  // This version exists in versions.json
          versions: {
            current: {
              label: '3.0.0-beta',
            },
            '2.0.0': {
              label: '2.0.0',
            },
          },
        },
      },
    ],
  ],
};
```

With `versions.json`:
```json
[
  "2.0.0",
  "1.0.0"
]
```

### Expected behavior

The configuration should be accepted without errors since `2.0.0` is a valid version that exists in the available versions. Instead, I'm getting an error message saying the lastVersion is invalid.

Also noticed something weird with `onlyIncludeVersions` - when I provide an array with version names, it throws an error about empty arrays not being allowed, which doesn't make sense.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
