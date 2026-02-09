# Bug Report

### Describe the bug

After a recent update, the response body assertion is not working correctly. When trying to check if a response body doesn't have a certain value, I'm getting syntax errors or the test just doesn't run at all.

### Reproduction

```js
const response = pm.response;

// This throws an error or doesn't work
pm.expect(response).to.not.have.body('expected text');
```

The issue seems to be related to the `not.have.body` assertion chain. It looks like the code got corrupted somehow - when I inspect the response object, the structure looks malformed with function definitions appearing in weird places.

### Expected behavior

The `not.have.body()` assertion should work properly to verify that the response body does NOT contain the expected text. This was working fine in the previous version.

### Additional context

I noticed this started happening after updating to the latest version. The positive assertion (`to.have.body`) seems to work fine, but the negative form (`to.not.have.body`) is broken.

---
Repository: /testbed
