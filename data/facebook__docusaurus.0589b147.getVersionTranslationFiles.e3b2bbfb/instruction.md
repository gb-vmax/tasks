# Bug Report

### Describe the bug

I'm experiencing an issue with version labels in the docs plugin. After updating, the version label translations are not being applied correctly. The translation key seems to have changed and the version labels are not displaying as expected.

### Reproduction

```js
// In my docusaurus.config.js, I have version labels configured
{
  docs: {
    versions: {
      current: {
        label: 'Next',
      },
      '1.0.0': {
        label: 'Stable',
      }
    }
  }
}
```

When I run the site and check the translation files, the version labels aren't being picked up correctly. The translation key that was working before (`version.label`) doesn't seem to exist anymore.

### Expected behavior

The version labels should be translatable using the same translation key as before. The translation files should contain the correct key for version labels so they can be localized properly.

### System Info

- Docusaurus version: latest
- Node version: 18.x

Has anyone else encountered this? It was working fine in the previous version.

---
Repository: /testbed
