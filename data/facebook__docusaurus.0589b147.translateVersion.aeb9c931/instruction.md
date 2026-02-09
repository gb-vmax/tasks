# Bug Report

### Describe the bug

I'm encountering an issue with version label translations in the docs plugin. When I set up custom version labels and translations, the translation file lookup seems to be using the wrong key, which causes the translation to fail silently.

### Reproduction

1. Create a versioned docs setup with a custom version label:
```js
// docusaurus.config.js
{
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          versions: {
            current: {
              label: 'Next 🚀',
              path: 'next',
            },
          },
        },
      },
    ],
  ],
}
```

2. Add a translation file for the version
3. Try to translate the version label using the translation system

### Expected behavior

The version label should use the translated message from the translation file. If no translation is found, it should fall back to the original label that was configured.

### Actual behavior

The translation lookup fails and falls back to an unexpected value instead of the configured label. The system appears to be looking up the translation file using one property but then falling back to a different property when the translation is missing.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
