# Bug Report

### Describe the bug

The logger's string interpolation is producing incorrect output when formatting messages with template strings. The interpolated values appear to be shifted or misaligned with their corresponding placeholders in the message template.

### Reproduction

```js
import logger from '@docusaurus/logger';

// Example usage that produces incorrect output
logger.info`Building path=${'docs'} for name=${'MyProject'}`;
```

The output appears garbled - the values don't match up with their intended placeholders. For example, 'docs' might appear where 'MyProject' should be, or parts of the message template itself are missing or duplicated.

### Expected behavior

The interpolated message should correctly substitute values into their corresponding placeholders, producing a properly formatted log message like:
```
Building path=docs for name=MyProject
```

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have started recently and affects all logger methods that use template string interpolation (info, warn, error, etc.).

---
Repository: /testbed
