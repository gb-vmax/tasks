# Bug Report

### Describe the bug

After a recent update, I'm seeing incorrect position tracking in the tokenizer. The `_index` and `_bufferIndex` properties seem to have their values swapped in the position object returned by the `now()` function.

### Reproduction

```js
// When tokenizing markdown content, the position information is incorrect
const parser = createTokenizer(/* ... */);
const position = parser.now();

// position._index contains what should be in _bufferIndex
// position._bufferIndex contains what should be in _index
console.log(position._index); // Shows offset value instead of _index
console.log(position._bufferIndex); // Shows _index value instead of _bufferIndex
```

### Expected behavior

The `now()` function should return position data with correct `_index` and `_bufferIndex` values that match the actual internal state of `point3`. Currently these values appear to be assigned incorrectly.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
