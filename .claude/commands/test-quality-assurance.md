# Test Quality Assurance Rules

## CRITICAL: Follow These Steps EXACTLY - No Deviations

### 1. Problem Resolution

- Use active file context or user-provided problem name
- If unclear, run: `uv run python -m leetcode_py.tools.check_test_cases --threshold=10 --max=1`

### 2. Test Reproducibility Verification Process

**MANDATORY 6-Step Process - Execute in Order:**

```bash
# Step 1: Backup original files
cp -r leetcode/{problem_name} leetcode/{problem_name}_backup

# Step 2: Regenerate from JSON template (use bake, NOT uv run)
bake p-gen -p {problem_name} -f

# Step 3: Restore original solution ONLY
cp leetcode/{problem_name}_backup/solution.py leetcode/{problem_name}/solution.py

# Step 4: Verify linting pass (CRITICAL for CI)
bake lint

# Step 5: Verify tests pass (expected to fail if solution is incomplete)
bake p-test -p {problem_name}

# Step 6: Cleanup
rm -rf leetcode/{problem_name}_backup
```

### 3. What NOT to Do

- ❌ **NEVER edit cookiecutter templates** (`{{cookiecutter.problem_name}}/` files)
- ❌ **NEVER use `uv run python -m leetcode_py.cli.main gen`** - use `bake p-gen` instead
- ❌ **NEVER modify helpers.py manually** - let regeneration handle it
- ❌ **NEVER skip ty verification** - this is the main CI issue
- ❌ **NEVER assume tests will pass** - they may fail if solution is incomplete

### 4. What to Do

- ✅ **ALWAYS use `bake p-gen -p {problem_name} -f`** for regeneration
- ✅ **ALWAYS verify ty passes** before considering task complete
- ✅ **ALWAYS restore original solution** after regeneration
- ✅ **ALWAYS check JSON template** if ty fails (look for `assert_assert_` bugs)

## Test Case Standards

### Coverage Requirements

- **Minimum 12 test cases** per problem
- **Edge cases**: Empty inputs, single elements, boundary values
- **Corner cases**: Maximum/minimum constraints, duplicates, sorted arrays
- **Normal cases**: Mixed scenarios with varied complexity

### JSON Format

- Use single quotes for Python strings: `'hello'` not `"hello"`
- Follow existing parametrize format
- Ensure valid Python list syntax in test_cases field

## Quick Commands

### CLI Commands (Recommended)

```bash
# Generate enhanced problem
uv run lcpy gen -s {problem_name} -o leetcode --force

# Test specific problem
bake p-test -p {problem_name}

# Lint check
bake lint
```

### Development Commands

```bash
# Find problems needing enhancement
uv run python -m leetcode_py.tools.check_test_cases --threshold=10

# Check all problems (no limit)
uv run python -m leetcode_py.tools.check_test_cases --threshold=10 --max=none

# Check with custom threshold
uv run python -m leetcode_py.tools.check_test_cases --threshold=12

# Generate from JSON template (uses uv run lcpy internally)
bake p-gen -p {problem_name} -f
```

## Common Issues & Solutions

### Issue: `assert_assert_missing_number` Error

**Cause**: JSON template has `helpers_assert_name: "assert_missing_number"` but template adds `assert_` prefix
**Solution**: Change JSON to `helpers_assert_name: "missing_number"` so template generates `assert_missing_number`

### Issue: ty Import Errors

**Cause**: Regenerated helpers.py doesn't match test imports
**Solution**: Use `bake p-gen` (not uv run) and verify JSON template is correct

### Issue: Tests Fail After Regeneration

**Expected**: Tests may fail if solution is incomplete (returns 0 or placeholder)
**Action**: This is normal - focus on ty passing, not test results

## Success Criteria

- ✅ **ty passes** with no errors (CRITICAL for CI)
- ✅ **Test structure matches JSON template** exactly
- ✅ **Original solution preserved** (user's code intact)
- ✅ **helpers.py generated correctly** (no `assert_assert_` bugs)
- ✅ **Reproducibility verified** (can regenerate consistently)

## When to Use This Workflow

- GitHub Actions CI failures due to ty errors
- Test reproducibility verification requests
- Need to ensure test structure matches JSON template
- CI test failures in reproducibility checks
