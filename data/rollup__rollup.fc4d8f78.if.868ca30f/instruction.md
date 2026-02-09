# Bug Report

### Describe the bug

I'm encountering an issue where log messages are being augmented multiple times, causing duplicate prefixes and other formatting issues in the output. It seems like the guard condition that's supposed to prevent re-augmentation isn't working correctly.

### Reproduction

```js
const log = {
  plugin: 'my-plugin',
  message: 'Something went wrong'
}

// First call augments the log
augmentLogMessage(log)

// Second call should be skipped but augments again
augmentLogMessage(log)
```

After the second call, the log message has duplicate formatting/prefixes applied to it.

### Expected behavior

The `augmentLogMessage` function should only augment a log message once. Subsequent calls with the same log object should be no-ops and return early without modifying the message.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
