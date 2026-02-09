# Bug Report

### Describe the bug

After a recent update, certificate paths with environment variable references are no longer working as expected. When I try to use `${ENV_VAR}` syntax in certificate file paths, the application tries to use the literal string instead of resolving the environment variable value.

### Reproduction

```js
const cert = new Certificate({
  name: 'my-cert',
  matches: ['https://example.com/*'],
  key: { src: '${CERT_KEY_PATH}/client.key' },
  cert: { src: '${CERT_PATH}/client.crt' }
});

// The paths are not being interpolated
// Expected: /actual/path/to/certs/client.key
// Actual: ${CERT_KEY_PATH}/client.key
```

### Steps to reproduce
1. Set up environment variables for certificate paths (e.g., `CERT_KEY_PATH=/path/to/certs`)
2. Create a Certificate object with paths containing `${ENV_VAR}` placeholders
3. The certificate fails to load because it's looking for files with literal `${...}` in the path

### Expected behavior
Certificate paths should support environment variable interpolation using `${VAR_NAME}` syntax, and these should be resolved to their actual values when the certificate is created.

### Additional context
This was working in previous versions. The environment variables are definitely set correctly - I can verify them in the shell. It seems like the interpolation step is missing or broken.

---
Repository: /testbed
