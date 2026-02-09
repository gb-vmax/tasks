# Bug Report

### Describe the bug
When importing Postman collections that contain scripts with `pm.*` API calls, the translation to `insomnia.*` is not working correctly. The resulting scripts have malformed syntax where parts of the original `pm.` prefix are duplicated or incorrectly preserved.

### Reproduction
1. Create a Postman collection with a pre-request or test script containing `pm.` API calls
2. Import the collection into Insomnia
3. Check the imported script content

Example script in Postman:
```js
pm.environment.set('token', 'abc123');
pm.test('Status is 200', function() {
  pm.response.to.have.status(200);
});
```

After import, the script appears corrupted with incorrect character placement.

### Expected behavior
The `pm.*` calls should be cleanly replaced with `insomnia.*` calls:
```js
insomnia.environment.set('token', 'abc123');
insomnia.test('Status is 200', function() {
  insomnia.response.to.have.status(200);
});
```

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking our team's migration from Postman to Insomnia. Any help would be appreciated!

---
Repository: /testbed
