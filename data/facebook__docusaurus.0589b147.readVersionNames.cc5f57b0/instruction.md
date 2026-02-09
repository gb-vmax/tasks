# Bug Report

### Describe the bug

When setting up versioned docs with `includeCurrentVersion: true`, the current version is being added to the versions array even when it's already explicitly listed in `versions.json`. This creates duplicate version entries and causes issues with version handling.

### Reproduction

1. Create a `versions.json` file that explicitly includes the current version:
```json
["current", "1.0.0"]
```

2. Configure the docs plugin with `includeCurrentVersion: true`:
```js
{
  includeCurrentVersion: true,
  // other options...
}
```

3. The versions array now contains duplicate "current" entries, which breaks the documentation versioning system.

### Expected behavior

The plugin should check if the current version is already present in `versions.json` before adding it. If it's already there, it shouldn't be added again. The logic should prevent duplicates regardless of the `includeCurrentVersion` setting.

### Additional context

This seems to have introduced a regression where the condition for adding the current version got inverted. Now it adds the current version when it's already present instead of when it's missing.

---
Repository: /testbed
