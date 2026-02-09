# Bug Report

### Describe the bug

The `expectValue` helper function in the date input test utilities is not working as expected. When I use it to verify that an input has a specific value, it passes when the values are different and fails when they match, which is the opposite of what should happen.

### Reproduction

```ts
import { render } from '@testing-library/react';
import { DateInput } from '@mantine/dates';
import { expectValue } from '@mantine-tests/dates';

const { container } = render(<DateInput value={new Date(2024, 0, 15)} />);

// This should pass but fails
expectValue(container, '01/15/2024');

// This should fail but passes
expectValue(container, 'wrong value');
```

### Expected behavior

The `expectValue` helper should verify that the input contains the expected value. It should pass when the actual value matches the expected value, and fail when they don't match.

### System Info

- @mantine/dates version: latest
- @mantine-tests/dates version: latest

---
Repository: /testbed
