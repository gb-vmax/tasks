# Bug Report

### Describe the bug

I'm experiencing an issue with version metadata properties in the docs plugin. The `badge` property seems to be displaying the wrong value, and the `isLast` flag appears to be inverted.

### Reproduction

When setting up versioned docs with the following configuration:

```js
{
  versions: {
    current: {
      label: 'Next',
      banner: 'unreleased',
      badge: true,
    },
    '1.0.0': {
      label: '1.0.0',
      banner: 'none',
      badge: false,
    }
  }
}
```

The version metadata props show:
- The `badge` property contains the value from `banner` instead of the actual badge configuration
- The `isLast` flag is reversed - versions that should be marked as last are not, and vice versa

### Expected behavior

- `badge` should reflect the badge configuration value, not the banner value
- `isLast` should correctly identify the last/latest version without being inverted

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is causing incorrect rendering of version badges and affecting version navigation logic.

---
Repository: /testbed
