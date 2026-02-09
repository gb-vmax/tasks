# Bug Report

### Describe the bug

When there are namespace conflicts due to re-exports, the warning message displays incorrect file paths. All three file references in the warning show the same file path instead of showing the actual conflicting sources.

### Reproduction

1. Create a module that re-exports the same binding from two different sources
2. Build the project with rollup
3. Observe the namespace conflict warning

The warning message shows something like:
```
"src/index.js" re-exports "foo" from both "src/index.js" and "src/index.js" (will be ignored).
```

Instead of showing the actual conflicting files like:
```
"src/index.js" re-exports "foo" from both "src/moduleA.js" and "src/moduleB.js" (will be ignored).
```

### Expected behavior

The warning should display:
- The file doing the re-export (reexporter)
- The first source file being re-exported from
- The second conflicting source file being re-exported from

All three paths should be different and accurately reflect the actual files involved in the conflict.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
