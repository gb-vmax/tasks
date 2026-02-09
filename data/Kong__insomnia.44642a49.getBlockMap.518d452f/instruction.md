# Bug Report

### Describe the bug

I'm experiencing an issue with text synchronization where the diff algorithm seems to be producing incorrect results. When trying to sync changes between documents, the block mapping appears to be broken, leading to corrupted or incomplete diffs.

### Reproduction

```js
// When syncing text changes with block-based diffing
const text1 = "Hello World! This is a test string for syncing.";
const text2 = "Hello World! This is a modified test string.";

// The diff operation produces unexpected results
const delta = diff(text1, text2);
// Delta contains incorrect block mappings
```

The issue manifests when:
1. Creating a diff between two text strings
2. The block hashing/mapping doesn't correctly identify matching blocks
3. Subsequent operations fail or produce corrupted output

### Expected behavior

The diff algorithm should correctly identify and map text blocks, producing accurate deltas that can be applied to synchronize documents. Each block should be properly hashed and stored in the block map for efficient comparison.

### System Info
- Package: @insomnia/sync
- Version: latest
- Node: 18.x

This seems to have started happening recently and is affecting document synchronization reliability. Any help would be appreciated!

---
Repository: /testbed
