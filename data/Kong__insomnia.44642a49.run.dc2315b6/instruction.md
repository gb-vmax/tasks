# Bug Report

### Describe the bug

I'm experiencing an issue with the JSONPath template tag where the function signature has been changed but the arguments array doesn't match. When trying to use the JSONPath tag, it seems like the new parameters (`returnAll` and `defaultValue`) aren't being properly defined in the `args` array, which causes the function to not work as expected.

### Reproduction

```js
// Using JSONPath template tag with the new parameters
const tag = {
  name: 'jsonpath',
  displayName: 'JSONPath',
  description: 'Extract values from JSON using JSONPath',
  args: [
    {
      displayName: 'JSON String',
      type: 'string',
    },
    {
      displayName: 'Filter',
      type: 'string',
    },
  ],
  run(_context, jsonString, filter, returnAll, defaultValue) {
    // Function expects 5 parameters but only 2 are defined in args
  }
}
```

When I try to use this tag in a template, the `returnAll` and `defaultValue` parameters are undefined because they're not included in the `args` array definition.

### Expected behavior

The `args` array should include definitions for all parameters that the `run` function accepts. If the function signature includes `returnAll` and `defaultValue` parameters, there should be corresponding entries in the `args` array like:

```js
args: [
  { displayName: 'JSON String', type: 'string' },
  { displayName: 'Filter', type: 'string' },
  { displayName: 'Return All', type: 'boolean' },  // Missing
  { displayName: 'Default Value', type: 'string' }  // Missing
]
```

Without these arg definitions, users can't actually pass values for these new parameters through the template tag interface.

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
