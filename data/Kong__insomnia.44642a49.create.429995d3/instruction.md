# Bug Report

### Describe the bug

When creating a new plugin data document, the `type` field is being passed incorrectly to `docCreate`, causing the type to be set in the wrong parameter position. This results in the document being created with an incorrect structure.

### Reproduction

```js
import * as pluginData from './models/plugin-data';

// Create a new plugin data document with custom fields
const newDoc = pluginData.create({
  pluginId: 'my-plugin',
  data: { someKey: 'someValue' }
});

// The document structure is incorrect
// Expected: type field should be set properly
// Actual: type is passed as the first argument instead of being merged with patch
```

### Expected behavior

The `create` function should properly merge the `type` field with the patch object before passing it to `docCreate`. The document should be created with the correct structure including both the type and any custom fields from the patch.

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
