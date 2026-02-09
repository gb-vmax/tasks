# Bug Report

### Describe the bug

I'm encountering an issue with plugin configuration where plugins without an explicit `id` option are not being grouped correctly. It seems like plugins are now being grouped under `undefined` instead of using the default plugin ID, which is causing unexpected behavior in my Docusaurus setup.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  plugins: [
    '@docusaurus/plugin-content-docs',
    '@docusaurus/plugin-content-docs', // duplicate plugin without id
  ],
};
```

When I have multiple instances of the same plugin without explicitly setting an `id` option, they should be grouped together under the default plugin ID. However, it appears they're being treated as having `undefined` as their ID instead.

### Expected behavior

Plugins without an explicit `id` should automatically use `DEFAULT_PLUGIN_ID` for grouping purposes. Multiple instances of the same plugin without IDs should be detected as duplicates and raise an appropriate error about duplicate plugin instances.

### System Info

- Docusaurus version: latest
- Node version: 18.x

This seems to have changed recently and is breaking my multi-instance plugin setup where I was relying on the default ID behavior.

---
Repository: /testbed
