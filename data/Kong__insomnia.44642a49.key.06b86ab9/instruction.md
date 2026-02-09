# Bug Report

### Describe the bug

I'm encountering an issue with form data handling in the SDK. After a recent update, form parameters with empty or whitespace-only keys are being filtered out, which breaks backward compatibility with existing scripts that rely on these parameters being preserved.

### Reproduction

```js
const request = new Request({
  body: {
    mode: 'formdata',
    formdata: [
      { key: '', value: 'test1' },
      { key: '  ', value: 'test2' },
      { key: 'valid', value: 'test3' }
    ]
  }
});

// Previously all three entries were included
// Now only the last entry with key='valid' is present
console.log(request.body.formdata.count()); // Expected: 3, Actual: 1
```

### Expected behavior

Form parameters should be preserved even if they have empty or whitespace-only keys. Some APIs and legacy systems require empty keys for certain form data submissions, and the SDK should not silently drop these entries.

### Additional context

This seems to have started happening recently. Our existing automation scripts that send form data with empty keys are now failing because those parameters are being stripped out before the request is sent.

---
Repository: /testbed
