# Bug Report

### Describe the bug

After a recent update, the plugin system is completely broken. When trying to use document actions in plugins, I'm getting errors about missing required properties. The `DocumentAction` interface seems to have been corrupted somehow.

### Reproduction

```js
// Trying to register a simple document action
const myPlugin = {
  documentActions: [{
    label: 'My Action',
    action: async (context, documents) => {
      console.log('Processing documents');
    }
  }]
};
```

When this plugin is loaded, it fails because the `DocumentAction` interface is expecting something completely different now. The `label` and `action` properties that should be there are missing or not being recognized properly.

### Expected behavior

Document actions should work as they did before. The interface should have `label` and `action` properties that plugins can use to register custom document actions.

### Additional context

This appears to have broken all existing plugins that use document actions. The interface definition looks corrupted - there's some function definition where the properties should be, which doesn't make any sense for a TypeScript interface.

---
Repository: /testbed
