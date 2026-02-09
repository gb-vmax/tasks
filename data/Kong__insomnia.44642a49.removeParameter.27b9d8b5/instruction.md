# Bug Report

### Describe the bug

The `removeParameter` method in the request context is not removing query parameters as expected. When I try to remove a parameter, it seems to be doing the opposite - keeping only the parameters I want to remove and deleting everything else.

### Reproduction

```js
// In a plugin script
const parameters = request.getParameters();
console.log('Before:', parameters); // Shows: [{name: 'foo', value: 'bar'}, {name: 'test', value: '123'}]

request.removeParameter('foo');

const updatedParameters = request.getParameters();
console.log('After:', updatedParameters); // Expected: [{name: 'test', value: '123'}]
                                          // Actual: [{name: 'foo', value: 'bar'}]
```

### Expected behavior

When calling `removeParameter('foo')`, the parameter named 'foo' should be removed from the request, and all other parameters should remain. Instead, it appears to be removing all parameters EXCEPT the one specified.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
