# Bug Report

### Describe the bug

I'm experiencing an issue with chunk assignment where static dependencies aren't being tracked correctly for entry points. It seems like the dependency relationships between chunks and entries are getting messed up, causing incorrect bundling behavior.

### Reproduction

```js
// Setup with multiple entry points
const config = {
  input: {
    entry1: 'src/entry1.js',
    entry2: 'src/entry2.js',
    entry3: 'src/entry3.js'
  }
}

// When chunks have dependencies on specific entries
// The first entry's dependencies seem to be lost
// and subsequent entries have incorrect dependency mappings
```

### Expected behavior

Each entry point should correctly track which chunks it depends on. When an entry has static dependencies on certain chunks, those dependencies should be properly recorded and not shifted or overwritten.

### Additional context

This appears to affect builds with multiple entry points where chunks are shared between entries. The dependency tracking for the first entry seems particularly problematic, and the mappings for other entries appear to be off by one position.

---
Repository: /testbed
