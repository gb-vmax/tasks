# Bug Report

### Describe the bug

I'm experiencing an issue with versioned docs directories not being resolved correctly when using plugin IDs. The path structure seems to be completely wrong - instead of looking in the expected location, it's generating an incorrect directory path.

### Reproduction

When I have a docs plugin with a custom plugin ID configured like this:

```js
{
  id: 'api',
  path: 'docs-api',
  // ... other config
}
```

And I try to use versioned docs, the plugin is looking for versioned content in the wrong directory structure.

Expected directory structure:
```
versioned_docs/
  version-1.0.0/
```

But it seems to be looking for something like:
```
versioned_docs/
  1.0.0-versioned_docs/
```

This breaks versioned docs functionality completely when using custom plugin IDs. The version name and directory name are being combined in an unexpected way.

### Expected behavior

The plugin should look for versioned docs in the standard `versioned_docs/version-{versionName}` directory structure, with the plugin ID prefix applied to the parent directory when needed, not mixed into the version folder name itself.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

---
Repository: /testbed
