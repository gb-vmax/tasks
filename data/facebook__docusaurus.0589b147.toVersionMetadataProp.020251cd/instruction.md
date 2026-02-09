# Bug Report

### Describe the bug

I'm experiencing an issue with the version metadata props in the docs plugin. The `banner` and `badge` properties appear to be swapped, and the `isLast` property is showing the opposite of what it should be.

### Reproduction

When I check the version metadata in my Docusaurus site, I notice:

1. The banner configuration is displaying where the badge should be
2. The badge configuration is displaying where the banner should be  
3. The `isLast` flag is inverted - versions that should be marked as last are not, and vice versa

For example, if I configure a version with:
```js
{
  banner: 'unreleased',
  badge: true,
  isLast: true
}
```

The actual rendered output shows the banner and badge switched, and `isLast` evaluates to false.

### Expected behavior

The version metadata props should correctly reflect the configured values:
- `banner` should contain the banner value
- `badge` should contain the badge value
- `isLast` should be true when the version is marked as the last version

### System Info

- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
