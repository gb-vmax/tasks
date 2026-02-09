# Bug Report

### Describe the bug

When configuring plugins or themes as arrays with a function and options object, the validation is failing unexpectedly. The config validation seems to be rejecting valid plugin configurations that should be accepted.

### Reproduction

```js
// docusaurus.config.js
module.exports = {
  plugins: [
    [
      require.resolve('./my-plugin'),
      {
        option1: 'value1',
        option2: 'value2'
      }
    ]
  ]
}
```

When starting Docusaurus with this configuration, I get a validation error even though this is the documented way to pass options to plugins.

### Expected behavior

The plugin configuration should be accepted when provided as a 2-element array with a function/string path as the first element and an options object as the second element. This is the standard format shown in the documentation.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
