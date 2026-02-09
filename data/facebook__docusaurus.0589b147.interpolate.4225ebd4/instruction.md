# Bug Report

### Describe the bug

The logger's interpolation function is not correctly handling format flags when interpolating values. When using format flags like `path=` or `name=` in log messages, the flag detection is looking at the wrong message segment, causing incorrect formatting to be applied to the interpolated values.

### Reproduction

```js
import logger from '@docusaurus/logger';

// This should format the path with the path formatter
logger.info`Processing file at path=${'some/file/path'}`;

// The format flag is not detected correctly and the value 
// gets formatted with the wrong formatter or no formatter at all
```

Another example:
```js
logger.info`Found url=${'https://example.com'} in code=${'const x = 1'}`;
// The url and code values don't get formatted with their respective formatters
```

### Expected behavior

When a format flag (like `path=`, `url=`, `code=`, `name=`, etc.) is specified before an interpolated value, the logger should detect that flag and apply the corresponding formatter to the value. The formatted output should reflect the appropriate styling/coloring for that value type.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
