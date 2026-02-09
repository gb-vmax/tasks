# Bug Report

### Describe the bug

I'm experiencing an issue with the remark parser where the `text` export from the constructs module is returning unexpected values. Instead of getting the original text construct, I'm getting what appears to be a stringified or modified version.

### Reproduction

```js
import { text } from './vendor/remark@15.0.1.js';

// Expecting to get the text construct object
console.log(text);
// Getting a function that returns string/null instead
```

When I try to use the `text` construct in my markdown parsing pipeline, it's not behaving as expected. The construct should be an object with tokenization rules, but it seems to be wrapped in some kind of transformation function.

### Expected behavior

The `text` export should return the actual text construct object (text2) directly, not a function that converts it to string or handles undefined/null cases. This is breaking compatibility with code that expects the standard construct format.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to have appeared recently and is affecting my markdown processing workflow. Any help would be appreciated!

---
Repository: /testbed
