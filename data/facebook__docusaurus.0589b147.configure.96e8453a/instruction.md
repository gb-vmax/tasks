# Bug Report

### Describe the bug

I'm experiencing an issue with MDX configuration where extensions are not being applied correctly. When passing an array of extensions to the MDX compiler, they seem to be processed in the wrong order or not merged properly with the base configuration.

### Reproduction

```js
const { compile } = require('@mdx-js/mdx');

const baseConfig = {
  remarkPlugins: [pluginA]
};

const extensions = [
  [pluginB, pluginC],
  pluginD
];

// Extensions don't get applied correctly
const result = await compile(content, {
  ...baseConfig,
  remarkPlugins: [...baseConfig.remarkPlugins, ...extensions]
});
```

### Expected behavior

All extensions should be properly merged with the base configuration and applied in the correct order. Nested arrays of extensions should be flattened and combined with the existing configuration.

### System Info

- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
