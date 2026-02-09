# Bug Report

### Describe the bug

I'm encountering an issue with BOM (Byte Order Mark) handling in file content. When processing files that start with a UTF-16 BOM, the BOM is not being stripped correctly, causing unexpected characters to appear at the beginning of the parsed content.

### Reproduction

```js
// File content with UTF-16 BE BOM (0xFEFF)
const content = '\uFEFF{"key": "value"}';
const stripped = stripBom(content);

// Expected: '{"key": "value"}'
// Actual: BOM character still present in output
console.log(stripped); // Still has BOM at start
```

### Expected behavior

The `stripBom` function should correctly identify and remove the UTF-16 Big Endian BOM (0xFEFF) from the beginning of string content. Currently it seems like files with this BOM are not being processed properly.

### Additional context

This is causing issues when trying to parse JSON files that have been saved with UTF-16 BE encoding. The leftover BOM character breaks JSON parsing and other text processing operations.

---
Repository: /testbed
