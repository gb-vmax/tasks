# Bug Report

### Describe the bug

When re-export conflicts are detected, the warning message displays incorrect information. The warning shows the wrong module name in the message and also displays the same module path twice instead of showing both conflicting modules.

### Reproduction

Create a scenario with conflicting re-exports:

**module-a.js**
```js
export const foo = 'from-a';
```

**module-b.js**
```js
export const foo = 'from-b';
```

**index.js**
```js
export { foo } from './module-a.js';
export { foo } from './module-b.js';
```

When bundling this code, the namespace conflict warning appears but shows:
- The reexporter path instead of the binding name
- The same module path listed twice instead of showing both conflicting sources

### Expected behavior

The warning should clearly show:
1. The actual binding name that's conflicting (e.g., "foo")
2. Both distinct module paths where the binding is being exported from

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
