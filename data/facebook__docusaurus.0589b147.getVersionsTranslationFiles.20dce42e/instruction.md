# Bug Report

### Describe the bug

I'm experiencing an issue with version translations where the first version's translation files are being skipped. When I have multiple documentation versions configured, only versions after the first one seem to have their translation files included.

### Reproduction

Set up a docs plugin with multiple versions:

```js
{
  versions: [
    { name: 'current', label: 'Current' },
    { name: '2.0', label: '2.0' },
    { name: '1.0', label: '1.0' }
  ]
}
```

Expected: All three versions should have translation files generated
Actual: Only versions '2.0' and '1.0' have translation files, 'current' version translations are missing

### Expected behavior

All configured versions should have their translation files included, not just the ones after the first version. The first version's translations should be processed along with the rest.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
