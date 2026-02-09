# Bug Report

### Describe the bug

When using `includeCurrentVersion: true` in the docs plugin configuration, the current version is being added to the versions list even when it's already explicitly defined in `versions.json`. This causes duplicate version entries and breaks the documentation site.

### Reproduction

1. Create a `versions.json` file that explicitly includes the current version:
```json
["current", "2.0.0", "1.0.0"]
```

2. Configure the docs plugin with `includeCurrentVersion: true`:
```js
{
  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        includeCurrentVersion: true,
      },
    ],
  ],
}
```

3. Build or start the site
4. The current version appears twice in the version dropdown/list

### Expected behavior

The current version should only appear once in the versions list. If it's already explicitly added to `versions.json`, it shouldn't be added again automatically. The `includeCurrentVersion` option should only add the current version when it's not already present.

### Additional context

This seems to have started happening recently. Previously, the plugin would check if the current version was already in the list before adding it.

---
Repository: /testbed
