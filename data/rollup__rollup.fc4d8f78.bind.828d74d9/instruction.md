# Bug Report

### Describe the bug

When exporting a default declaration in a module, the naming logic for the default export variable appears to be inverted. If there's already a variable with the same name in the scope, the export gets the base name instead of the suffixed version, and vice versa.

### Reproduction

```js
// module.js
const MyModule = { foo: 'bar' };
export default MyModule;
```

When bundling this module, if there's a naming conflict with an existing variable in the scope, the default export variable name assignment seems backwards. The `_default` suffix is being applied in the wrong case - it gets added when there's no conflict and omitted when there is a conflict.

### Expected behavior

The default export variable should:
- Use the base module name when there's no naming conflict
- Use the `_default` suffixed name when there IS a conflict with an existing variable

Currently it appears to be doing the opposite.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
