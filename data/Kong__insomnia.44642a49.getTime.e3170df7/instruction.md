# Bug Report

### Describe the bug

The `getTime()` method in the response context is not working as expected after a recent update. When I try to call it without any arguments (which should return the elapsed time in milliseconds), I'm getting an error or unexpected behavior.

### Reproduction

```js
// In a plugin script
const time = insomnia.response.getTime();
console.log(time); // Should return elapsed time in ms
```

The method used to work fine when called without arguments, but now it seems like something changed with how the time is being returned.

### Expected behavior

Calling `getTime()` without any parameters should return the elapsed time in milliseconds, just like it did before. The basic usage shouldn't break when new optional features are added.

### Additional context

I noticed this after updating to the latest version. My plugin relies on getting the response time for logging purposes, and the simple `getTime()` call is now causing issues. I haven't changed my plugin code at all.

---
Repository: /testbed
