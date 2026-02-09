# Bug Report

### Describe the bug

After a recent update, the DocumentAction interface seems to be malformed. When trying to use document actions in plugins, I'm getting TypeScript errors saying that `action` and `label` properties are missing from the interface definition.

### Reproduction

```ts
// Trying to define a document action
const myDocumentAction: DocumentAction = {
  label: 'My Action',
  action: async (context, documents) => {
    // do something
  }
};
```

TypeScript complains that the object doesn't match the DocumentAction interface. Looking at the type definition, it seems like the interface properties got replaced with function definitions somehow.

### Expected behavior

The DocumentAction interface should have the `action` and `label` properties properly defined so plugins can implement document actions without type errors.

### System Info
- Insomnia version: latest
- TypeScript version: 5.x

---
Repository: /testbed
