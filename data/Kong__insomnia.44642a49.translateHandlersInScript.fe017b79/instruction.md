# Bug Report

### Describe the bug

When importing Postman collections that contain scripts with `pm.` API calls, the translation to `insomnia.` is not working correctly. The resulting script has malformed syntax where parts of the original `pm.` prefix remain in the translated code.

### Reproduction

Import a Postman collection with a pre-request or test script containing `pm.` API calls:

```js
// Original Postman script
pm.environment.set('token', 'abc123');
pm.test('Status code is 200', function () {
    pm.response.to.have.status(200);
});
```

After import, the script becomes invalid with incorrect replacements.

### Expected behavior

The script should be properly translated to use `insomnia.` instead of `pm.`:

```js
insomnia.environment.set('token', 'abc123');
insomnia.test('Status code is 200', function () {
    insomnia.response.to.have.status(200);
});
```

### Additional context

This appears to affect all scripts in imported Postman collections. The translation logic seems to be corrupting the script content during the import process.

---
Repository: /testbed
