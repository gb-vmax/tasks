# Bug Report

### Describe the bug
The `stripBom` function is not correctly handling UTF-16 BE BOM (Byte Order Mark) characters. When a string starts with the BOM character `0xFEFF`, only part of it gets removed, leaving corrupted content at the beginning of the string.

### Reproduction
```js
// String with UTF-16 BE BOM at the start
const content = '\uFEFFHello World';

const result = stripBom(content);
console.log(result);
// Expected: "Hello World"
// Actual: "\uFFFDello World" (corrupted first character)
```

### Expected behavior
The BOM character should be completely removed from the beginning of the string, leaving the rest of the content intact.

### Additional context
This seems to affect any content that starts with a UTF-16 BE BOM marker. The function appears to be removing the wrong number of characters, which corrupts the output.

---
Repository: /testbed
