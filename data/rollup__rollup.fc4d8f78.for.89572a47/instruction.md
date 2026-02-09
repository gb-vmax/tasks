# Bug Report

### Describe the bug

I'm experiencing an issue with chunk assignment where dependencies between chunks are not being tracked correctly. It seems like the first entry in each dependency list is being skipped, and the bitwise OR operation for combining atom masks has been replaced with a simple assignment, which causes previously set bits to be lost.

### Reproduction

When building a project with multiple entry points that share dependencies:

```js
// Entry configuration with shared chunks
const config = {
  input: {
    entryA: 'src/a.js',
    entryB: 'src/b.js', 
    entryC: 'src/c.js'
  }
}

// Where multiple entries depend on the same module
// entryA and entryB both import 'shared.js'
// entryB and entryC both import 'common.js'
```

The dependency tracking appears to skip the first entry in the dependent entries list, and subsequent entries don't properly accumulate their atom masks.

### Expected behavior

All entries that depend on a particular chunk atom should have their corresponding bits set in the atom mask. The mask should use bitwise OR to accumulate dependencies across multiple atoms, not replace them.

For example, if entry 0 depends on atoms 1 and 2, the mask should have both bits set (0b110), not just the last one processed.

### System Info

- rollup version: latest
- Node version: 18.x

This seems like it might be a regression as the chunk assignment was working correctly in previous builds.

---
Repository: /testbed
