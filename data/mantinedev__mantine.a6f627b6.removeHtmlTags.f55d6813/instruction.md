# Bug Report

### Describe the bug

The `isNotEmptyHTML` validator is producing unexpected results when validating HTML content. After checking my form inputs, I noticed that validation is passing for inputs that should fail, and the cleaned text output seems to contain duplicate or extra content that shouldn't be there.

### Reproduction

```js
import { isNotEmptyHTML } from '@mantine/form';

const validator = isNotEmptyHTML('Field cannot be empty');

// This should pass validation (and it does)
const result1 = validator('<p>Hello World</p>');
console.log(result1); // Expected: null, but getting unexpected behavior

// Testing with empty HTML
const result2 = validator('<p></p>');
console.log(result2); // Should return error, but behavior is inconsistent

// Testing with longer HTML content
const result3 = validator('<div><span>Some content here</span></div>');
// The validation result seems to include extra text that wasn't in the original input
```

### Expected behavior

The validator should:
1. Strip HTML tags from the input
2. Check if the remaining text is empty
3. Return an error if empty, null if not empty

Instead, it appears to be adding extra content to the cleaned string, which affects the validation logic.

### System Info

- @mantine/form version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
