# GitHub Actions Automation Guide

## Overview

This project uses GitHub Actions for Continuous Integration (CI) automation. The workflow automatically tests and lints the code on every push and pull request.

## Workflow Location

```
.github/workflows/ci.yml
```

## What It Does

The CI pipeline runs two jobs on Ubuntu:

### 1. Test Job
- Checks out the code
- Sets up Python 3.11
- Installs dependencies from `requirements.txt`
- Runs the test suite (`test_app.py`)

### 2. Lint Job
- Checks out the code
- Sets up Python 3.11
- Installs flake8
- Runs linting checks for syntax errors and code quality

## Triggers

The workflow runs automatically when:
- You push to `main` or `master` branch
- You create a pull request to `main` or `master` branch

## How to Use

### 1. Push to GitHub

```bash
git add .
git commit -m "Your commit message"
git push origin main
```

### 2. View Results

After pushing:
1. Go to your repository on GitHub
2. Click on the **Actions** tab
3. Select the workflow run to view details
4. Check if all jobs passed (green checkmark) or failed (red X)

### 3. Fix Failed Workflows

If a job fails:
- **Test failure**: Check your code and ensure the server responds correctly
- **Lint failure**: Run `flake8` locally to find and fix issues

## Customize the Workflow

### Change Python Version

Edit `.github/workflows/ci.yml`:
```yaml
with:
  python-version: "3.10"  # Change to your version
```

### Add More Branches

Edit the `on` section:
```yaml
on:
  push:
    branches: [ "main", "master", "develop" ]
```

### Add Deployment (CD)

To add Continuous Deployment, extend the workflow:

```yaml
deploy:
  needs: [test, lint]
  runs-on: ubuntu-latest
  if: github.ref == 'refs/heads/main'
  steps:
    - name: Deploy to production
      run: echo "Deploy your app here"
```

## Local Testing Before Push

Run tests locally before pushing:

```bash
python test_app.py
```

Run linting locally:

```bash
pip install flake8
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```

## Badges

Add a status badge to your README.md:

```markdown
![CI/CD Pipeline](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/ci.yml/badge.svg)
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Workflow not running | Check if you're pushing to the correct branch |
| Tests failing | Ensure the FastAPI server can start and respond |
| Permission errors | Go to Settings > Actions and enable workflows |

## Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Python Actions Templates](https://github.com/actions/starter-workflows/tree/main/ci)
- [FastAPI Testing](https://fastapi.tiangolo.com/tutorial/testing/)
