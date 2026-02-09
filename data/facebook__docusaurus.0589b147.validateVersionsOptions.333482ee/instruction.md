# Bug Report

### Describe the bug

The validation for `onlyIncludeVersions` option in the docs plugin is throwing errors in the wrong cases. When I provide a valid configuration with an empty array or when `lastVersion` is correctly included in `onlyIncludeVersions`, I'm getting validation errors that shouldn't be happening.

### Reproduction

**Case 1: Empty array validation**
```js
// docusaurus.config.js
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          onlyIncludeVersions: [], // Should throw error but doesn't
        },
      },
    ],
  ],
};
```

Expected: Should throw error about empty array
Actual: No error is thrown

**Case 2: lastVersion validation**
```js
// docusaurus.config.js
module.exports = {
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          onlyIncludeVersions: ['1.0.0', '2.0.0'],
          lastVersion: '2.0.0', // This IS in the array
        },
      },
    ],
  ],
};
```

Expected: Should work fine since '2.0.0' is in the array
Actual: Throws error saying lastVersion must be present in onlyIncludeVersions array

### Expected behavior

- When `onlyIncludeVersions` is an empty array, it should throw a validation error
- When `lastVersion` is present in the `onlyIncludeVersions` array, it should NOT throw an error

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
