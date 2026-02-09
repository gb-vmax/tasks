# Bug Report

### Describe the bug

The `useLogger` hook is not logging component updates correctly. When props change, the hook logs the mount message instead of the update message, and when the component name changes, it logs updates even though the props haven't changed.

### Reproduction

```jsx
import { useLogger } from '@mantine/hooks';

function MyComponent({ value }) {
  useLogger('MyComponent', [value]);
  
  return <div>{value}</div>;
}

// When value prop changes from 'initial' to 'updated':
// Expected: "MyComponent updated [updated]"
// Actual: "MyComponent mounted [updated]"
```

Also, if I change the component name but keep the same props, it still logs an update:

```jsx
const [name, setName] = useState('ComponentA');

function TestComponent({ data }) {
  useLogger(name, [data]);
  return <div>{data}</div>;
}

// Changing name triggers update log even though data prop is unchanged
setName('ComponentB');
```

### Expected behavior

- Mount logs should only appear when the component actually mounts
- Update logs should appear when props change
- Changing the component name shouldn't trigger update logs if props haven't changed

### System Info
- @mantine/hooks version: latest
- React version: 18.x

---
Repository: /testbed
