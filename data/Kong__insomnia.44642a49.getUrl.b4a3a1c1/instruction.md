# Bug Report

### Describe the bug

After a recent update, the plugin context's `getUrl()` method is not working correctly. When I try to call it in my plugin, I get a syntax error and the plugin fails to load.

### Reproduction

```js
module.exports.requestHooks = [
  context => {
    const url = context.request.getUrl();
    console.log(url);
  }
];
```

When the plugin runs, it throws an error and the request hook doesn't execute. The issue seems to have appeared after the latest changes to the request context API.

### Expected behavior

The `getUrl()` method should return the full request URL as a string without any errors. This was working fine before the update.

### Additional context

I noticed the code for `getUrl()` looks malformed in the source file - there seems to be some function definitions that aren't properly structured. The helper functions `parseUrlWithParams` and `reconstructUrl` appear to be defined outside of the context object but are referenced inside it.

---
Repository: /testbed
