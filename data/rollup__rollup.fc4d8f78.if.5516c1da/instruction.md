# Bug Report

### Describe the bug

I'm experiencing an issue with plugin caching where plugins with certain names are not being cached correctly. It seems like the logic for determining whether a plugin should be cacheable has a problem.

### Reproduction

When I create a plugin with a name that doesn't start with the anonymous prefixes and hasn't been registered yet, it's being marked as non-cacheable when it should be cacheable.

```js
const myPlugin = {
  name: 'my-custom-plugin',
  // ... other plugin properties
}

// This plugin should be cacheable, but it's being treated as non-cacheable
```

Also noticed that plugins with names containing certain output plugin prefix strings in the middle of their name are incorrectly being marked as non-cacheable.

### Expected behavior

- Plugins with unique names (not starting with anonymous prefixes) should be cacheable
- Only plugins whose names *start with* the anonymous output plugin prefix should be treated specially, not those that merely contain it somewhere in the name
- The caching logic should correctly identify when a plugin name is new vs already existing

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
