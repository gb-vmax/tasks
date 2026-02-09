# Bug Report

### Describe the bug

When displaying circular dependency warnings, the output is inconsistent with the expected behavior. When there are exactly 5 circular dependencies, the CLI is showing 4 dependencies followed by a "...and 1 more" message instead of displaying all 5 dependencies directly.

### Reproduction

Create a project with exactly 5 circular dependencies and run the build. The warning output will show:

```
Circular dependencies
dependency1 -> dependency2 -> dependency1
dependency3 -> dependency4 -> dependency3
dependency5 -> dependency1 -> dependency5
dependency2 -> dependency3 -> dependency2
...and 1 more
```

### Expected behavior

When there are 5 or fewer circular dependencies, all of them should be displayed without the "...and X more" message. The truncation should only happen when there are more than 5 dependencies.

Expected output for 5 dependencies:
```
Circular dependencies
dependency1 -> dependency2 -> dependency1
dependency3 -> dependency4 -> dependency3
dependency5 -> dependency1 -> dependency5
dependency2 -> dependency3 -> dependency2
dependency4 -> dependency5 -> dependency4
```

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
