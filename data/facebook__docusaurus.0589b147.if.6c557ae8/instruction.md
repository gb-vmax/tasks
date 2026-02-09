# Bug Report

### Describe the bug

I'm experiencing an issue with version banners in the docs plugin. The banner logic seems to be inverted - the current/latest version is now showing a banner when it shouldn't, and older versions are not showing banners when they should.

### Reproduction

Set up a docs site with multiple versions:
```js
// docusaurus.config.js
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          versions: {
            current: {
              label: '2.0.0',
            },
          },
        },
      },
    ],
  ],
};
```

With versions: `current`, `1.0.0`, `0.9.0`

**Expected behavior:**
- Current version (2.0.0): No banner should appear
- Older versions (1.0.0, 0.9.0): Should show appropriate version banners

**Actual behavior:**
- Current version (2.0.0): Shows a banner (shouldn't happen)
- Older versions: No banner appears (should show banners)

The banner display logic appears to be backwards. This makes the documentation confusing for users as they can't tell which version they're viewing.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
