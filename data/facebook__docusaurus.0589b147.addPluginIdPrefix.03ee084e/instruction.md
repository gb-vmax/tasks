# Bug Report

### Describe the bug

When using multiple plugin instances with `docusaurus-plugin-content-docs`, the versioned directories are being created with incorrect naming. The plugin ID prefix is being added to the wrong instances - it's appearing on the default plugin instance instead of the non-default instances.

### Reproduction

1. Configure multiple docs plugin instances in `docusaurus.config.js`:
```js
{
  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'default',
        // ... other config
      },
    ],
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'community',
        // ... other config
      },
    ],
  ],
}
```

2. Create versioned docs for both instances
3. Check the generated directory names

### Expected behavior

- Default plugin instance should create directories like: `versioned_docs/version-1.0.0`
- Non-default plugin instances should create directories with prefix like: `community_versioned_docs/version-1.0.0`

### Actual behavior

The directory naming is reversed - the default instance gets the prefix when it shouldn't, and non-default instances don't get the prefix when they should.

This appears to be a logic error in how the plugin ID prefix is being applied to version file paths.

---
Repository: /testbed
