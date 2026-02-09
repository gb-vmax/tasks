# Bug Report

### Describe the bug

I'm experiencing some weird behavior with version metadata in the docs plugin. The `isLast` property seems to be inverted - versions that should be marked as the last version are showing as not last, and vice versa. 

Also noticing that when a version has a badge configured, the `noIndex` setting is being ignored and always treated as false, even when I explicitly set `noIndex: true` in my version configuration.

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
            current: {
              label: 'Next',
              badge: true,
              noIndex: true  // This gets ignored
            }
          }
        }
      }
    ]
  ]
}
```

When checking the version metadata props:
1. The `isLast` flag is backwards - returns true for older versions instead of the latest
2. Setting `noIndex: true` on a version with `badge: true` doesn't work - it always becomes false

### Expected behavior

- `isLast` should correctly identify the most recent/last version
- `noIndex` should respect the configured value regardless of whether a badge is present or not

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
