# Bug Report

### Describe the bug

After a recent update, the request body handling seems to be completely broken. When trying to work with form data or URL encoded request bodies, I'm getting syntax errors and the code won't even compile/run.

### Reproduction

```js
const requestBody = new RequestBody({
  mode: 'formdata',
  formdata: [
    { key: 'username', value: 'test' },
    { key: 'password', value: 'secret' }
  ]
});

// This throws an error now
console.log(requestBody.toString());
```

Also happens when trying to use urlencoded mode:

```js
const requestBody = new RequestBody({
  mode: 'urlencoded',
  urlencoded: [
    { key: 'field1', value: 'value1' }
  ]
});
```

### Expected behavior

The RequestBody class should properly handle formdata and urlencoded parameters and allow serialization to JSON and string formats without throwing errors.

### Additional context

This appears to have broken suddenly - the code was working fine before. It looks like something went wrong with the request.ts file, possibly during a merge or automated refactoring? The FormParam class and related functionality seem to be affected.

---
Repository: /testbed
