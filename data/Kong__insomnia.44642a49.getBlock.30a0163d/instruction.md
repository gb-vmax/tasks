# Bug Report

### Describe the bug

The delta diff algorithm is producing incorrect hash values for blocks, which causes sync operations to fail when comparing strings. When diffing two strings, the block hashes don't match what they should be, leading to incorrect delta operations being generated.

### Reproduction

```js
import { diff } from './sync/delta/diff';

const source = "hello world";
const target = "hello there world";
const blockSize = 5;

const operations = diff(source, target, blockSize);
// The operations generated are incorrect due to wrong block hashing
```

When trying to sync data between clients, the diff algorithm generates operations that don't properly represent the changes between the source and target strings. This results in corrupted data after applying the delta operations.

### Expected behavior

The diff function should correctly hash each block of the source string and generate accurate delta operations that can be applied to transform the source into the target. Block hashes should only include the content of that specific block, not the entire remaining string.

### System Info
- Package: insomnia
- Module: sync/delta/diff.ts

---
Repository: /testbed
