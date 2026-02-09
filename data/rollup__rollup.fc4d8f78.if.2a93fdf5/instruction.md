# Bug Report

### Describe the bug

I'm encountering an issue where log messages are not being augmented properly. It seems like the augmentation logic is skipping logs that should be processed, resulting in missing plugin information and location details in the output.

### Reproduction

```js
const log = {
  plugin: 'my-plugin',
  message: 'Something went wrong',
  // loc is undefined
}

augmentLogMessage(log)

// Expected: log message should be augmented with plugin prefix
// Actual: log message remains unchanged
```

Also happens when `loc` is present but `plugin` is missing:

```js
const log = {
  // plugin is undefined
  loc: { file: 'test.js', line: 10 },
  message: 'Error occurred'
}

augmentLogMessage(log)

// Expected: log message should be augmented with location info
// Actual: log message remains unchanged
```

### Expected behavior

The `augmentLogMessage` function should augment logs that have either a `plugin` OR a `loc` property (or both). Currently it seems to be requiring both properties to be present, which means logs with only one of these properties are being skipped.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
