# Bug Report

### Describe the bug

When there are conflicting re-exports from multiple modules, the warning message displays the same module path twice instead of showing both conflicting sources. This makes it impossible to identify which two modules are actually causing the conflict.

### Reproduction

Create a scenario with namespace conflicts:

1. Set up a module that re-exports the same binding from two different sources
2. Build the project
3. Check the warning output

The warning message shows something like:
```
"module.js" re-exports "something" from both "source1.js" and "source1.js" (will be ignored).
```

But it should show:
```
"module.js" re-exports "something" from both "source1.js" and "source2.js" (will be ignored).
```

### Expected behavior

The warning should display both conflicting module paths so developers can identify and resolve the actual conflict. Currently it's showing the first source twice, which doesn't help in debugging the issue.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
