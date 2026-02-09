# Bug Report

### Describe the bug

File watcher is not properly tracking changes on transformed/aliased file paths. When a file is accessed through a transform/alias (like when using path mappings or virtual modules), the watcher invalidates the original file path instead of the transformed one, causing the build system to miss updates.

### Reproduction

```js
// Setup with a path transform/alias
const watcher = new FileWatcher({
  transformPath: (id) => {
    // Transform paths, e.g., alias resolution
    return id.replace('@/', './src/');
  }
});

// Watch a file through its transformed path
watcher.watch('@/components/Button.vue');

// Modify the actual file at ./src/components/Button.vue
// The watcher detects the change but invalidates '@/components/Button.vue' 
// instead of the transformed path './src/components/Button.vue'
// Result: build doesn't recognize the file needs to be rebuilt
```

### Expected behavior

When a file change is detected and `transformWatcherId` is set, the watcher should invalidate using the transformed ID (`changedId`) rather than the original ID. This ensures that the build system properly tracks dependencies through path transformations.

### System Info
- OS: Linux / FreeBSD
- Node version: 18.x

The issue seems related to how the file watcher handles the invalidation call - it's using the wrong identifier when transforms are involved.

---
Repository: /testbed
