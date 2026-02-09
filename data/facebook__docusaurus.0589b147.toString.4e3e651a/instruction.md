# Bug Report

### Describe the bug

I'm experiencing an issue with the `toString()` method in VFile. When I try to convert a VFile object to a string, it's returning an empty string instead of the actual content, even when the file has valid content.

### Reproduction

```js
const file = new VFile({value: 'Hello world'});
console.log(file.toString()); // Expected: "Hello world", Actual: ""
```

Also noticed that when the value is already a string, it seems to be doing something weird:

```js
const file = new VFile({value: 'test content'});
const result = file.toString();
// Result is empty string instead of "test content"
```

### Expected behavior

The `toString()` method should return the string representation of the file's value. If the value is a string, it should return that string directly. If the value is undefined, it should return an empty string.

### System Info

- remark version: 15.0.1
- Node.js version: Latest

This seems to have broken recently - the method used to work correctly before. Any help would be appreciated!

---
Repository: /testbed
