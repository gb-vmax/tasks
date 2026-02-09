# Bug Report

### Describe the bug

I'm experiencing an issue with the docs plugin version validation where it's not throwing errors when it should. Specifically, when I configure unknown version names in the `versions` option, the plugin doesn't catch the error and just continues silently. Similarly, when I set `lastVersion` to a version that's not included in `onlyIncludeVersions`, it also fails to validate properly.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          versions: {
            'nonexistent-version': {
              label: 'Test',
            },
          },
        },
      },
    ],
  ],
};
```

In this case, I would expect an error to be thrown about `nonexistent-version` not being a valid version, but the build proceeds without any warnings.

Another case:

```js
docs: {
  lastVersion: '2.0.0',
  onlyIncludeVersions: ['1.0.0', '1.5.0'],
}
```

Here `lastVersion` is set to `2.0.0` but it's not in the `onlyIncludeVersions` array. This should throw a validation error but doesn't.

### Expected behavior

The plugin should throw validation errors when:
1. Unknown version names are configured in the `versions` option
2. `lastVersion` is set to a value not present in `onlyIncludeVersions`

This validation was working correctly before, so this seems like a regression.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
