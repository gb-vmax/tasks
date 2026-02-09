# Bug Report

### Describe the bug

When using the docs plugin with multiple versions, the first version is not being translated. All other versions are correctly translated, but the first version in the versions array always appears in the original language even when translation files are provided.

### Reproduction

```js
const versions = [
  { name: 'current', label: 'Current' },
  { name: '2.0', label: 'Version 2.0' },
  { name: '1.0', label: 'Version 1.0' }
];

// After translation, only versions[0] ('current') remains untranslated
// versions[1] and versions[2] are correctly translated
```

Steps to reproduce:
1. Set up a docs plugin with multiple versions
2. Add translation files for all versions
3. Build the site
4. The first version displays in the original language while other versions are translated

### Expected behavior

All versions should be translated when translation files are available, including the first version in the array.

### System Info
- Docusaurus version: latest
- Plugin: @docusaurus/plugin-content-docs

---
Repository: /testbed
