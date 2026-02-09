# Bug Report

### Describe the bug

I'm experiencing an issue where the `banner` and `badge` properties appear to be swapped in the version metadata. When I set a banner configuration for a docs version, it shows up as a badge instead, and vice versa.

### Reproduction

```js
// In docusaurus.config.js
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          versions: {
            current: {
              label: 'Next',
              banner: 'unreleased',
              badge: true,
            },
          },
        },
      },
    ],
  ],
};
```

When I configure a version with `banner: 'unreleased'` and `badge: true`, the banner configuration ends up being applied to the badge and the badge configuration is applied to the banner. So instead of seeing an "unreleased" banner at the top of the docs, I see it as a badge, and the badge setting controls the banner display.

### Expected behavior

The `banner` property should control the version banner display (e.g., showing "unreleased" or "unmaintained" banners), and the `badge` property should control whether a version badge is shown. They shouldn't be swapped.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
