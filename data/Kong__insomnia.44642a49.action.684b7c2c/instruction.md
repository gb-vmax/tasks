# Bug Report

### Describe the bug

The DocumentAction interface definition appears to be corrupted. When trying to use or extend document actions in plugins, the interface structure is completely broken and contains function implementation code instead of proper type definitions.

### Reproduction

```ts
// Attempting to define a document action
const myDocumentAction: DocumentAction = {
  label: 'My Action',
  action: async (context, documents) => {
    // do something
  }
}
```

This fails because the DocumentAction interface doesn't have the expected structure anymore.

### Expected behavior

The DocumentAction interface should define the proper shape for document actions with properties like:
- `label`: string
- `action`: function signature
- `hideAfterClick`: optional boolean

Instead, the interface definition seems to have been replaced with actual implementation code for `getDocumentActions()` function, which shouldn't be inside the interface block at all.

### System Info
- Insomnia version: latest
- TypeScript errors when trying to implement document actions

---
Repository: /testbed
