# Bug Report

### Describe the bug

The logger is not handling Date objects correctly anymore. When trying to log a Date object, it throws an error instead of formatting it properly.

### Reproduction

```js
import logger from '@docusaurus/logger';

const now = new Date();
logger.info`Current time: ${now}`;
```

This throws:
```
TypeError: msg.toUTCString is not a function
```

### Expected behavior

Date objects should be formatted using `toUTCString()` and logged without errors, just like before.

### Additional context

This seems to have broken recently. Previously logging Date objects worked fine and would display them in UTC format. Now it's causing the logger to crash when encountering Date instances.

---
Repository: /testbed
