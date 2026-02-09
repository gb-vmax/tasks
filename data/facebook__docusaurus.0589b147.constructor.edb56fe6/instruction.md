# Bug Report

### Describe the bug
Git initialization is failing silently in the test utilities. When trying to create a new Git instance for testing purposes, the repository initialization succeeds but the constructor throws an error, preventing any git operations from being performed.

### Reproduction
```js
import { Git } from './utils/git';
import os from 'os';
import path from 'path';

// Create a temporary directory
const tempDir = path.join(os.tmpdir(), 'test-repo');

// Try to initialize git - this throws an error unexpectedly
const git = new Git(tempDir);
```

The error message shows:
```
Error: git init exited with code 0.
derr: 
dout: Initialized empty Git repository...
```

### Expected behavior
The Git constructor should successfully initialize a repository when `git init` returns exit code 0 (success). The repository should be ready for commits and other git operations.

### Additional context
This seems to happen consistently when creating new Git instances. The git command itself is working fine (exit code 0 means success), but the constructor is treating it as a failure condition.

---
Repository: /testbed
