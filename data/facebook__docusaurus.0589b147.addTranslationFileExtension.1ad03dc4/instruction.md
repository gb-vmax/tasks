# Bug Report

### Describe the bug

When specifying translation file paths, the system now rejects paths that already include the `.json` extension, even though the error message suggests the opposite behavior. The validation logic appears to be inverted.

### Reproduction

```js
// This now throws an error unexpectedly
const filePath = 'translations/en.json';
// Error: Translation file path at "translations/en.json" does not need to end with ".json", we add the extension automatically.

// But this is accepted (which seems wrong)
const filePath2 = 'translations/en';
// No error, but the extension is not added as the message claims
```

### Expected behavior

Based on the error message, paths ending with `.json` should be accepted (since the extension is supposedly added automatically). Or if paths should NOT include `.json`, then paths without the extension should have it added automatically.

Currently the behavior is inconsistent with what the error message states.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
