# Bug Report

### Describe the bug

When I have multiple entry modules with mixed exports and rollup displays the warning, the entry modules are shown in reverse alphabetical order instead of alphabetical order. Also, when there are more than 5 warnings, only 4 are displayed instead of the first 3.

### Reproduction

Create a project with multiple entry modules that mix named and default exports:

```
entry-a.js
entry-b.js  
entry-c.js
entry-d.js
entry-e.js
entry-f.js
```

All modules export both named and default exports. When building, the MIXED_EXPORTS warning displays the modules in the wrong order (f, e, d, c instead of a, b, c, d).

Additionally, if you have 6+ modules, it shows 4 entries before the "...and X other entry modules" message instead of 3.

### Expected behavior

The warning should list entry modules in alphabetical order (a, b, c, d...) and when there are more than 5 warnings, it should display the first 3 entries before showing the "...and X other entry modules" message.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
