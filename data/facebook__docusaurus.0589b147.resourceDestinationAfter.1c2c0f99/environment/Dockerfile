FROM augustinemp/swesmith.docusaurus.0589b147:latest
WORKDIR /testbed
# Clean up Docker image build artifacts (duplicate repo directories and Dockerfiles)
# These are left over from the image build process and can confuse test runners
RUN rm -rf /testbed/*__*.* /testbed/Dockerfile.* 2>/dev/null || true
COPY bug.patch /tmp/bug.patch
RUN git apply /tmp/bug.patch || git apply --reject /tmp/bug.patch || patch -p1 < /tmp/bug.patch
RUN rm /tmp/bug.patch
# Remove test directories and files so agent can't run tests (restored during verification)
RUN find /testbed -type d \( -name 'test' -o -name 'tests' -o -name '__tests__' -o -name 'spec' -o -name 'specs' -o -name '__mocks__' -o -name 'e2e' -o -name '__e2e__' -o -name 'integration-tests' -o -name 'unit-tests' -o -name '__fixtures__' -o -name 'fixtures' -o -name 'test-fixtures' -o -name '__snapshots__' -o -name 'testing' -o -name 'testUtils' -o -name 'test-utils' \) -exec rm -rf {} + 2>/dev/null || true && \
    find /testbed -type f \( -name '*.test.js' -o -name '*.test.ts' -o -name '*.test.jsx' -o -name '*.test.tsx' -o -name '*.test.mjs' -o -name '*.test.cjs' -o -name '*.tests.js' -o -name '*.tests.ts' -o -name '*.tests.jsx' -o -name '*.tests.tsx' -o -name '*.spec.js' -o -name '*.spec.ts' -o -name '*.spec.jsx' -o -name '*.spec.tsx' -o -name '*.spec.mjs' -o -name '*.spec.cjs' -o -name 'test_*.py' -o -name '*_test.py' -o -name '*_tests.py' -o -name '*.test.coffee' -o -name '*.spec.coffee' -o -name 'jest.config.js' -o -name 'jest.config.ts' -o -name 'jest.config.mjs' -o -name 'jest.config.cjs' -o -name 'jest.setup.js' -o -name 'jest.setup.ts' -o -name 'vitest.config.js' -o -name 'vitest.config.ts' -o -name 'vitest.config.mjs' \) -delete 2>/dev/null || true
# Squash git history to hide the bug change
RUN rm -rf .git && \
    git init && \
    git config user.email "dev@example.com" && \
    git config user.name "Developer" && \
    git add -A && \
    git commit -m "Initial commit"
