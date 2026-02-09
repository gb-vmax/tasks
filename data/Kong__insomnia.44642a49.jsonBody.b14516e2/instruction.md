# Bug Report

### Describe the bug

There seems to be an issue with the response object code. When trying to use `insomnia.response.to.have.jsonBody()`, the code appears to be malformed and contains unexpected content mixed into the implementation.

### Reproduction

Looking at the response.ts file, the `jsonBody` method in the `to.have` section contains what looks like example usage code mixed directly into the implementation:

```js
jsonBody: (expected: object) => {
    if (expected && typeof expected === 'object' && '$partial' in expected && expected.$partial === true) {
        const matchObj = '$match' in expected ? expected.$match : expected;
        return haveJsonBody(matchObj, true, true);
    }
    return haveJsonBody(expected, true, false);
}

 insomnia.response.to.have.jsonBody(expectedObject)  // <-- This shouldn't be here
```

The line `insomnia.response.to.have.jsonBody(expectedObject)` appears to be documentation or example code that got accidentally included in the actual implementation.

### Expected behavior

The `jsonBody` method should only contain the implementation logic without any example usage code embedded in it. This is likely causing syntax errors or unexpected behavior when the code is parsed/executed.

### System Info
- Insomnia SDK version: latest
- Affected file: packages/insomnia-sdk/src/objects/response.ts

---
Repository: /testbed
