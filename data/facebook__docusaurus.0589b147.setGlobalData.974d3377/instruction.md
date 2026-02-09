# Bug Report

### Describe the bug

I'm experiencing an issue with plugin global data where accessing data from plugins throws an error. It seems like the global data structure isn't being initialized correctly before data is assigned to it.

### Reproduction

When using `setGlobalData` in a plugin's `contentLoaded` lifecycle, I get an error:

```js
// In a plugin
async contentLoaded({content, actions}) {
  actions.setGlobalData({
    myData: 'some value'
  });
}
```

This throws an error because it's trying to access a property on `undefined`.

### Expected behavior

The `setGlobalData` action should properly initialize the nested structure before assigning data. Plugins should be able to set their global data without errors.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
