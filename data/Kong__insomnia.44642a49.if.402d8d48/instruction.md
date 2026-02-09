# Bug Report

### Describe the bug

I'm experiencing an issue with the `replaceSubstitutions` method in the SDK. When I try to use it with variables, it's not working as expected. The method seems to be incomplete or broken in the latest version.

### Reproduction

```js
const Property = require('insomnia-sdk').Property;

const template = "Hello {{name}}, welcome to {{place}}!";
const vars = { name: "John", place: "Insomnia" };

const result = Property.replaceSubstitutions(template, vars);
console.log(result);
```

When I run this code, I get unexpected behavior. The substitution doesn't complete properly.

### Expected behavior

The method should replace the template variables with the actual values from the variables object and return: `"Hello John, welcome to Insomnia!"`

### Additional context

This was working fine before, but after the recent update it seems like something broke. Not sure if this is related to some refactoring or if it's a regression.

---
Repository: /testbed
