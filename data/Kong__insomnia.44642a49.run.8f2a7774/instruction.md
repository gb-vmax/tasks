# Bug Report

### Describe the bug

I'm experiencing an issue with the OS template tag where it's throwing errors when trying to access array elements using bracket notation. The template tag seems to have issues with filter parsing and is not handling array index access properly.

### Reproduction

```js
// Using the OS template tag with array index filter
{% os 'cpus', '[0]' %}
```

When I try to use the OS template tag with a filter like `[0]` to access the first CPU, I get unexpected behavior. The filter doesn't seem to be processed correctly and the result is not what I expect.

### Expected behavior

The template tag should:
1. Accept array index notation like `[0]` in the filter parameter
2. Return the element at that index when the OS function returns an array
3. Handle the filter parameter consistently regardless of whether it's being used with JSONPath or simple array access

### Additional context

This seems to be related to how the filter parameter is being processed. The template tag appears to be trying to handle both JSONPath queries and simple array indexing, but something is off with the logic.

I'm using this in request templates where I need to access specific CPU information or other OS-related array data. Right now I have to work around this by not using filters at all.

---
Repository: /testbed
