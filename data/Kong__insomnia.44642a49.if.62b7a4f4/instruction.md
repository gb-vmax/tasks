# Bug Report

### Describe the bug

I'm experiencing an issue with the `replaceSubstitutions` method in the Property class. After a recent update, the method appears to be incomplete or corrupted. When I try to use variable substitution in my requests, the application crashes or behaves unexpectedly.

### Reproduction

```js
const Property = require('insomnia-sdk').Property;

const context = {
  baseUrl: 'https://api.example.com',
  endpoint: '/users'
};

const template = '{{baseUrl}}{{endpoint}}';

// This should replace the variables with their values
const result = Property.replaceSubstitutions(template, context);
console.log(result); // Expected: https://api.example.com/users
```

### Expected behavior

The `replaceSubstitutions` method should process the template string and replace all variable placeholders (e.g., `{{baseUrl}}`) with their corresponding values from the context object. The method should return a fully resolved string with all substitutions applied.

### Actual behavior

The method doesn't work as expected. It seems like the implementation is broken or incomplete, causing the substitution logic to fail.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

This is blocking our workflow as we rely heavily on variable substitution for our API requests. Any help would be appreciated!

---
Repository: /testbed
