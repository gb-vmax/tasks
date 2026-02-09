# Bug Report

### Describe the bug

I'm experiencing an issue with the remark processor where error handling seems to be inverted. When processing markdown content, errors are being rejected when there's no error, and successful transformations are being treated as errors.

### Reproduction

```js
const {remark} = require('remark');

const processor = remark();

// This should succeed but throws an error instead
processor.process('# Hello World', (err, file) => {
  if (err) {
    console.log('Got error:', err); // This gets called unexpectedly
  } else {
    console.log('Success:', file); // This never gets called
  }
});

// Using promises also shows the inverted behavior
processor.process('# Test')
  .then(result => {
    console.log('Should get here on success');
  })
  .catch(error => {
    console.log('Ends up here instead:', error); // Gets called on success
  });
```

### Expected behavior

When processing valid markdown without errors, the success callback/promise resolution should be triggered. Errors should only be thrown when actual processing errors occur.

Currently it seems like the error handling logic is backwards - successful processing triggers error handlers and vice versa.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
