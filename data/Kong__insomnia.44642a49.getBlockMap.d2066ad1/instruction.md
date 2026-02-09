# Bug Report

### Describe the bug

After a recent update, the sync delta diff algorithm seems to be creating duplicate block entries in the block map, which is causing significant performance degradation when syncing large documents. The sync operation that used to take a few seconds now takes several minutes, and memory usage has increased substantially.

### Reproduction

```js
// Syncing a document with repeating patterns
const doc1 = "a".repeat(1000) + "b".repeat(1000);
const doc2 = "a".repeat(1000) + "c" + "b".repeat(1000);

// Running diff on these documents causes excessive memory usage
// and takes much longer than expected
```

The issue becomes more pronounced with larger documents or documents that have repeating character sequences. It seems like the block map is being populated with many more entries than necessary.

### Expected behavior

The diff algorithm should efficiently handle documents with repeating patterns without creating redundant block entries. Sync operations should complete in a reasonable time frame similar to previous versions.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking our ability to sync large API collections. Any help would be appreciated!

---
Repository: /testbed
