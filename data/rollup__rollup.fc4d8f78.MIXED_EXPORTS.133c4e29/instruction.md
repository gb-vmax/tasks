# Bug Report

### Describe the bug

When there are 5 or more entry modules with mixed exports warnings, the CLI displays the wrong modules in the warning output. Instead of showing the first 3 modules, it's showing modules 2-4 (skipping the first one).

### Reproduction

Create a project with 5+ entry modules that mix named and default exports:

```js
// entry1.js
export default 'default1';
export const named1 = 'named1';

// entry2.js
export default 'default2';
export const named2 = 'named2';

// entry3.js
export default 'default3';
export const named3 = 'named3';

// entry4.js
export default 'default4';
export const named4 = 'named4';

// entry5.js
export default 'default5';
export const named5 = 'named5';
```

Run rollup with these entry points. The warning message shows:
```
The following entry modules are using named and default exports together:
entry2.js
entry3.js
entry4.js
...and 2 other entry modules
```

### Expected behavior

The warning should display the first 3 entry modules (entry1.js, entry2.js, entry3.js) when there are 5 or more warnings, not skip the first one. The "...and X other entry modules" count also seems off - it should say "...and 2 other entry modules" but the actual count might be incorrect.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
