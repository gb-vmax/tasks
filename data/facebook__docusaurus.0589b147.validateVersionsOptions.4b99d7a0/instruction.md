# Bug Report

### Describe the bug

When configuring the docs plugin with a valid `lastVersion` option, I'm getting an error saying the version is invalid, even though it exists in my available versions. The validation seems to be rejecting valid configurations.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          lastVersion: '2.0.0',
          versions: {
            current: {
              label: '3.0.0',
            },
            '2.0.0': {
              label: '2.0.0',
            },
            '1.0.0': {
              label: '1.0.0',
            },
          },
        },
      },
    ],
  ],
};
```

With this configuration, I get an error:
```
Docs option lastVersion: 2.0.0 is invalid. Available version names are: current, 2.0.0, 1.0.0
```

But `2.0.0` is clearly in the list of available versions!

### Expected behavior

The configuration should be accepted since `lastVersion: '2.0.0'` is present in the available versions. The site should build successfully without throwing a validation error.

### Additional context

This also happens when using `onlyIncludeVersions` together with `lastVersion`:

```js
docs: {
  lastVersion: '2.0.0',
  onlyIncludeVersions: ['current', '2.0.0', '1.0.0'],
}
```

This throws an error saying `lastVersion` must be present in `onlyIncludeVersions`, even though it is.

---
Repository: /testbed
