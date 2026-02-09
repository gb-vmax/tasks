# Bug Report

### Describe the bug

The warning message for `NAMESPACE_CONFLICT` is displaying incorrect information. When there's a namespace conflict with re-exports, the warning shows the same module path multiple times instead of showing the actual conflicting modules.

### Reproduction

Create a module that re-exports the same binding from two different modules:

```js
// module-a.js
export const foo = 'a';

// module-b.js
export const foo = 'b';

// reexporter.js
export { foo } from './module-a.js';
export { foo } from './module-b.js';
```

When building, the warning message will show something like:
```
"reexporter.js" re-exports "./module-a.js" from both "./module-a.js" and "./module-a.js" (will be ignored).
```

### Expected behavior

The warning should correctly display both conflicting module paths, like:
```
"reexporter.js" re-exports "foo" from both "./module-a.js" and "./module-b.js" (will be ignored).
```

The message should show:
1. The binding name being re-exported
2. The first module path
3. The second (conflicting) module path

Currently it's showing the same module path repeated instead of the actual conflicting modules.

---
Repository: /testbed
