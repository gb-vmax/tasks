# Bug Report

### Describe the bug

I'm experiencing an issue with export default declarations where the generated variable names are incorrect when there's a naming conflict with existing variables in the scope. 

The problem occurs when a module has both a named export and a default export with the same base name. Instead of properly handling the conflict by appending `_default` to the export default variable name, it seems like the logic is inverted - it's adding the suffix when there's NO conflict and using the plain name when there IS a conflict.

### Reproduction

```js
// module.js
export const myModule = 'named export';
export default function myModule() {
  return 'default export';
}
```

When bundling this, the default export gets assigned the variable name `myModule` even though that name is already taken by the named export, causing a naming collision. It should be using `myModule_default` instead.

### Expected behavior

When there's already a variable with the same name in the scope, the default export should automatically get renamed to `<name>_default` to avoid conflicts. When there's no conflict, it should use the plain name without the suffix.

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing build failures in our project where we have modules that export both named and default exports with matching names.

---
Repository: /testbed
