# Bug Report

### Describe the bug

I'm experiencing an issue with plugin global data when using multiple plugin instances. It appears that global data is being overwritten incorrectly, causing data from one plugin instance to be lost or assigned to the wrong key.

### Reproduction

```js
// Plugin configuration with multiple instances
module.exports = {
  plugins: [
    ['my-plugin', { id: 'instance1' }],
    ['my-plugin', { id: 'instance2' }],
  ],
};

// In the plugin
export default function myPlugin(context, options) {
  return {
    name: 'my-plugin',
    async contentLoaded({ content, actions }) {
      actions.setGlobalData({ someData: 'value for ' + options.id });
    },
  };
}
```

When I try to access the global data for different plugin instances, the data structure doesn't match what I expect. It seems like the second instance overwrites data from the first instance, or the data is being stored under the wrong plugin ID key.

### Expected behavior

Each plugin instance should have its global data stored separately under its respective plugin ID. When using `setGlobalData`, the data should be accessible via the correct plugin name and instance ID combination without overwriting data from other instances.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
