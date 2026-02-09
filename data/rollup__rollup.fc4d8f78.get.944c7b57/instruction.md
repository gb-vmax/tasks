# Bug Report

### Describe the bug

I'm experiencing an issue where the AST (Abstract Syntax Tree) is not being retrieved correctly from the cache. When a module's AST is requested, it seems like the logic for checking whether the AST exists in the LRU cache is inverted, causing the system to always try to parse the AST even when it's already cached.

### Reproduction

```js
// Setup a module with caching enabled
const module = new Module({
  // ... module config
  cache: true
});

// First access - parses and caches the AST
const ast1 = module.info.ast;

// Second access - should retrieve from cache but appears to re-parse
const ast2 = module.info.ast;
```

### Expected behavior

When the AST is already in the LRU cache, it should be retrieved directly from the cache without re-parsing. The cache lookup should return the cached value on subsequent accesses.

### Additional context

This seems to be causing performance issues as the AST is being parsed multiple times for the same file instead of being served from the cache. The cache hit logic appears to be backwards - it's returning cached values when they don't exist and parsing when they do exist.

---
Repository: /testbed
