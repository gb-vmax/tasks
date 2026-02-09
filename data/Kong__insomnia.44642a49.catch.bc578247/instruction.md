# Bug Report

### Describe the bug
After a recent update, JSON stringification is broken in the prettify utility. When trying to stringify objects, I'm getting empty strings returned instead of the expected JSON output.

### Reproduction
```js
import { ensureStringify } from './utils/prettify/json';

const testObj = {
  name: 'test',
  value: 123
};

const result = ensureStringify(testObj);
console.log(result); // Returns empty string instead of '{"name":"test","value":123}'
```

### Expected behavior
The function should return a valid JSON string representation of the object. Instead, it's returning an empty string for all object inputs.

### Additional context
This seems to have started happening after the latest changes to the json.ts file. String inputs still work fine, but any object passed to the function returns an empty string.

---
Repository: /testbed
