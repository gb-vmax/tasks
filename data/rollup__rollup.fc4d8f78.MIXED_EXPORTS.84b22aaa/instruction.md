# Bug Report

### Describe the bug

When multiple entry modules trigger the `MIXED_EXPORTS` warning, they appear to be displayed in the wrong order. The warning messages show entry modules in reverse alphabetical order instead of the expected alphabetical order.

### Reproduction

Create a project with multiple entry modules that mix named and default exports:

```js
// entry-a.js
export default 'a';
export const foo = 1;

// entry-b.js  
export default 'b';
export const bar = 2;

// entry-c.js
export default 'c';
export const baz = 3;
```

Build with rollup and observe the warning output. The entries are listed in reverse order (c, b, a) instead of alphabetical order (a, b, c).

### Expected behavior

Entry modules should be listed in alphabetical order in the warning message, making it easier to scan through the list when dealing with many entry points.

### Additional context

This affects readability when you have many entry modules with mixed exports. The inconsistent ordering makes it harder to quickly identify which modules need attention.

---
Repository: /testbed
