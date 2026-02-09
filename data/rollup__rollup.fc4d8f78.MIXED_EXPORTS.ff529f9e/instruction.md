# Bug Report

### Describe the bug

When bundling with more than 5 entry modules that have mixed named and default exports, the warning message incorrectly displays "...and X other entry modules" even when all modules are already shown in the list.

### Reproduction

Create a bundle configuration with exactly 5 entry modules that mix named and default exports:

```js
// entry1.js through entry5.js
export default function() {}
export const named = 'value'
```

Build the project and observe the warning output. You'll see something like:

```
Mixing named and default exports
The following entry modules are using named and default exports together:
entry1.js
entry2.js
entry3.js
entry4.js
...and 1 other entry modules

Consumers of your bundle will have to use chunk.default to access their default export...
```

### Expected behavior

When there are 5 or fewer entry modules with mixed exports, all of them should be displayed without the "...and X other entry modules" message. The truncation message should only appear when there are actually more modules than what's being displayed.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
