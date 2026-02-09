# Bug Report

### Describe the bug

I'm experiencing an issue with markdown processing where extensions are not being configured correctly. When I try to use custom handlers or extensions, they either don't get applied at all or the configuration seems to skip the first extension in the array.

### Reproduction

```js
const processor = remark()
  .use(somePlugin, {
    extensions: [
      extensionOne,
      extensionTwo,
      extensionThree
    ]
  });

// The first extension appears to be skipped
// Only extensionTwo and extensionThree are applied
```

### Expected behavior

All extensions in the array should be processed and applied in order. The first extension should not be skipped during configuration.

### Additional context

This seems to have started happening recently. When I configure multiple extensions or handlers, the first one in the list doesn't seem to take effect. The configuration loop might be starting at the wrong index.

---
Repository: /testbed
