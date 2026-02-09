# Bug Report

### Describe the bug

When generating chunk names for modules, duplicate chunk names are being created incorrectly. The chunk name collision detection seems to be happening after the cache is set, which causes subsequent calls with the same module path to return the base name instead of the numbered variant.

### Reproduction

```js
// First call with a module that generates chunk name "abc"
const name1 = genChunkName('/path/to/module1.js', 'prefix');
// Returns: "prefix---abc"

// Second call with different module that also generates "abc"
const name2 = genChunkName('/path/to/module2.js', 'prefix');
// Returns: "prefix---abc2" (correct)

// Third call with the first module again
const name3 = genChunkName('/path/to/module1.js', 'prefix');
// Returns: "prefix---abc" (should return "prefix---abc" from cache, which is correct)

// But if we call with module2 again:
const name4 = genChunkName('/path/to/module2.js', 'prefix');
// Returns: "prefix---abc2" (incorrect - should be from cache but collision counter increments)
```

The issue is that when a module path is seen again, it should return the cached chunk name, but the collision detection logic runs before caching, causing inconsistent results.

### Expected behavior

Once a chunk name is generated for a module path, subsequent calls with the same module path should always return the same cached chunk name without triggering collision detection again.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
