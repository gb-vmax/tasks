# Bug Report

### Describe the bug
The `replaceSubstitutions` method is throwing an error when it should be working correctly. When I pass valid parameters (a string and variable objects), it throws an error saying the types are incorrect, even though they are correct.

### Reproduction
```js
const Property = require('./properties');

// This should work but throws an error
const result = Property.replaceSubstitutions(
  'Hello {{name}}',
  { name: 'World' }
);
```

The error message says:
```
Error: replaceSubstitutions: the first param's type is not string or other parameters are not an array
```

But I'm clearly passing a string as the first parameter and an object as the second parameter, which should be valid according to the method signature.

### Expected behavior
The method should process the template string with the provided variables and return the substituted result. It should only throw an error when the parameters are actually invalid (e.g., when content is NOT a string or variables are NOT in an array-like format).

### Additional context
This seems like the validation logic might be inverted. The method is rejecting valid inputs instead of invalid ones.

---
Repository: /testbed
