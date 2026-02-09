# Bug Report

### Describe the bug

The `isNotEmptyHTML` validator is not correctly detecting empty HTML content. It seems to be treating HTML with only opening tags (like `<br>`, `<img>`, etc.) as valid non-empty content, even when there's no actual text.

### Reproduction

```js
import { isNotEmptyHTML } from '@mantine/form';

const validator = isNotEmptyHTML('Field cannot be empty');

// These should be considered empty but are passing validation
validator('<br>'); // Returns null (no error)
validator('<img src="test.jpg">'); // Returns null (no error)
validator('<div></div>'); // Returns null (no error)
validator('<p><br></p>'); // Returns null (no error)
```

### Expected behavior

The validator should return an error for HTML that contains only tags without any actual text content. Self-closing tags and empty paired tags should be considered as empty content.

### System Info
- @mantine/form version: latest
- Browser: Chrome 120

---
Repository: /testbed
