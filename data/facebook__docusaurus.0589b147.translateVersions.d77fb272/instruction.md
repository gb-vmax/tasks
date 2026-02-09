# Bug Report

### Describe the bug

I'm experiencing an issue with version translations where the wrong version is being translated. It seems like the versions are being shifted - each version gets the translation of the next version instead of its own.

### Reproduction

```js
const versions = [
  { name: 'current', label: 'Current' },
  { name: '2.0', label: '2.0' },
  { name: '1.0', label: '1.0' }
]

// After translation:
// - 'current' gets translations from '2.0'
// - '2.0' gets translations from '1.0'
// - '1.0' gets undefined/crashes
```

When I have multiple documentation versions configured, the translated labels and content are completely mismatched. The first version displays content from the second version, the second from the third, and the last version either shows nothing or causes errors.

### Expected behavior

Each version should receive its own corresponding translations, not the translations from the next version in the array.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
