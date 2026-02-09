# Bug Report

### Describe the bug

Log messages are not being augmented properly when either `plugin` or `loc` properties are present. The augmentation logic seems to have changed and now requires both properties to be present, which breaks the expected behavior.

### Reproduction

```js
const log = {
  plugin: 'my-plugin',
  message: 'Something went wrong'
  // no loc property
}

augmentLogMessage(log)
// Expected: log message should be augmented with plugin prefix
// Actual: log message is not augmented
```

Another case:

```js
const log = {
  loc: { file: 'index.js', line: 10 },
  message: 'Parse error'
  // no plugin property
}

augmentLogMessage(log)
// Expected: log message should be augmented with location info
// Actual: log message is not augmented
```

### Expected behavior

The log message should be augmented when **either** the `plugin` property **or** the `loc` property is present. Previously this was working correctly, but now it seems like both properties are required for augmentation to occur.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
