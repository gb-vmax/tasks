# Bug Report

### Describe the bug

I'm encountering an issue where the remark parser is failing to properly export the `text` construct. When trying to use the text construct from the module, I'm getting unexpected behavior - it appears the export is now wrapped in a function that returns either `undefined` or a stringified version of `text2`, rather than directly exporting the `text2` value itself.

### Reproduction

```js
import { text } from './vendor/remark@15.0.1.js';

// text is now a function instead of the expected construct object
console.log(text); // Expected: construct object, Actual: function

// Using it as a construct fails
const result = someParser.use(text);
// TypeError: Expected construct, got function
```

### Expected behavior

The `text` export should directly reference `text2` (the actual construct object), not be wrapped in a function. It should be consistent with other exports like `flowInitial`, `insideSpan`, and `string` which are exported as direct references.

### Additional context

This seems to have broken the markdown parsing functionality. The export statement for `text` appears malformed compared to the other exports in the same object.

---
Repository: /testbed
