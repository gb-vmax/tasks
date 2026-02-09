# Bug Report

### Describe the bug

The `getAncestors` function is broken after a recent change. When I try to use it in my templates, I'm getting syntax errors and the templating engine fails to render.

### Reproduction

```js
// In a template tag
const ancestors = await request.getAncestors(currentRequest);
```

This used to work fine but now throws an error when the template is evaluated. The entire request fails to execute.

### Expected behavior

The `getAncestors` function should return the ancestor documents (request groups and workspaces) for a given request, excluding the request itself. It should work the same way it did before.

### Additional context

This seems to have started happening after some recent changes to the templating system. The function appears to be malformed in the code - looks like there's a function definition in the wrong place or something got mangled during a refactor.

---
Repository: /testbed
