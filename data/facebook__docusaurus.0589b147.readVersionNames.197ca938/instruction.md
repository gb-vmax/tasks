# Bug Report

### Describe the bug

When setting `includeCurrentVersion: false` in the docs plugin options, the current version is still being added to the version list. The configuration option appears to be inverted - setting it to `false` includes the current version, and setting it to `true` excludes it.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          includeCurrentVersion: false, // Should exclude current version
          // ... other options
        },
      },
    ],
  ],
};
```

After building the site with this configuration, the current version still appears in the version dropdown and is accessible in the docs.

### Expected behavior

When `includeCurrentVersion` is set to `false`, the current version should not be included in the version list. When set to `true` (or omitted, as it defaults to true), the current version should be included.

### Additional context

This seems to affect sites that want to only show versioned docs without the "Next" or current development version. The workaround is to set `includeCurrentVersion: true` to actually exclude it, but this is confusing and counterintuitive.

---
Repository: /testbed
