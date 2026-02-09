# Bug Report

### Describe the bug

After a recent update, the `replaceSubstitutions` method appears to be broken. The method is not completing its execution and seems to be cut off mid-implementation. When trying to use property substitution with variables, the function doesn't work at all.

### Reproduction

```js
const Property = require('./properties');

const content = "Hello {{name}}, welcome to {{place}}!";
const variables = { name: "John", place: "Insomnia" };

// This fails to execute properly
const result = Property.replaceSubstitutions(content, variables);
console.log(result);
```

Expected output: `"Hello John, welcome to Insomnia!"`
Actual output: The method doesn't complete execution

### Additional context

It looks like the method implementation got corrupted or wasn't fully committed. The code seems to stop abruptly and the original substitution logic is missing. This is blocking our ability to use dynamic variables in requests.

### System Info
- Package: insomnia-sdk
- Version: latest

---
Repository: /testbed
