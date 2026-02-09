# Bug Report

### Describe the bug
After a recent update, the plugin API's `response.getTime()` method is completely broken and returns `undefined` instead of the elapsed time value. This is breaking all my plugins that rely on timing information.

### Reproduction
```js
// In a response hook plugin
module.exports.responseHooks = [
  context => {
    const time = context.response.getTime();
    console.log(time); // Expected: number (e.g., 150), Actual: undefined
  }
];
```

### Expected behavior
`response.getTime()` should return the elapsed time in milliseconds as a number, just like it did before.

### Additional context
This seems to have broken after some changes to the response context API. The method just returns undefined now when called without any arguments, which is how it's always been used in the documentation and existing plugins.

---
Repository: /testbed
