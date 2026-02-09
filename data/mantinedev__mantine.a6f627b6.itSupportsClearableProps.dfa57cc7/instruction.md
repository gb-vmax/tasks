# Bug Report

### Describe the bug

When using the `clearable` prop on date input components, the clear button cannot be found by its aria-label in certain scenarios. The component seems to render the clear button, but querying for it using `aria-label` fails inconsistently.

### Reproduction

```tsx
import { render, screen } from '@testing-library/react';

const Component = () => (
  <DateInput
    clearable
    clearButtonProps={{ 'aria-label': 'test-clear' }}
    rightSection="test-right-section"
  />
);

render(<Component />);

// This query fails to find the clear button
const clearButton = screen.getByLabelText('test-clear');
```

Additionally, when passing custom props to the clear button via `clearButtonProps`, the attributes don't seem to be applied correctly when querying by aria-label.

```tsx
<DateInput
  clearable
  clearButtonProps={{
    'aria-label': 'test-clear',
    'data-test-attr': 'value'
  }}
/>

// Cannot find button by aria-label
const button = screen.getByLabelText('test-clear');
```

### Expected behavior

The clear button should be consistently queryable using its aria-label. Custom props passed through `clearButtonProps` should be accessible on the rendered button element.

### System Info
- @mantine/dates: latest
- React: 18.x

---
Repository: /testbed
