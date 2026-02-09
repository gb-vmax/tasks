# Bug Report

### Describe the bug

I'm experiencing an issue with the remark tokenizer where accessing properties on the `info.from` object causes errors. It seems like the code is trying to access `info.from` directly as a value, but it should be accessing a property on it instead.

### Reproduction

```js
const parser = createParser();
const tokenizer = createTokenizer(parser, initializeFunc, fromValue);

// When tokenizer processes constructs, it fails
// The onsuccessfulconstruct callback receives info.from 
// but tries to use it incorrectly
```

### Expected behavior

The tokenizer should properly handle the `info.from` parameter when processing successful constructs. Currently getting errors when the construct is processed because `info.from` is being passed directly instead of accessing the correct property.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
