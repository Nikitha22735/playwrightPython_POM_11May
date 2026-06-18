# GitHub Actions CI/CD Pipeline with Allure Report on GitHub Pages

## Overview
This GitHub Actions workflow automatically runs Playwright tests, generates Allure reports, and deploys them to GitHub Pages for easy access and sharing.

## Workflow Configuration

### File Location
`.github/workflows/playwrightPython.yml`

### Workflow Triggers
- On push to `main` or `develop` branches
- On pull requests to `main` or `develop` branches

## Setup Instructions

### Step 1: Enable GitHub Pages

1. Go to your GitHub repository
2. Navigate to **Settings** → **Pages**
3. Under "Build and deployment":
   - **Source**: Select "Deploy from a branch"
   - **Branch**: Select "gh-pages" (this branch is auto-created by the workflow)
   - **Folder**: Select "/ (root)"
4. Click **Save**

### Step 2: Verify Repository Permissions

Ensure your repository has the following settings:
- **Settings** → **Actions** → **General**
- Under "Workflow permissions":
  - ☑ **Read and write permissions** (should be enabled for workflow to deploy)
  - ☑ **Allow GitHub Actions to create and approve pull requests**

### Step 3: Push Code

Once GitHub Pages is enabled, just push your code:
```bash
git add .
git commit -m "Add Playwright tests with Allure reporting"
git push origin main
```

## Workflow Steps

| Step | Action | Purpose |
|------|--------|---------|
| 1 | Set up Python | Install Python 3.10 runtime |
| 2 | Git Clone | Checkout repository code |
| 3 | Install Dependencies | Install requirements and Playwright browsers |
| 4 | Run Tests | Execute pytest with Allure results collection |
| 5 | Install Allure | Download and install Allure command-line tool |
| 6 | Generate Allure Report | Create HTML report from test results |
| 7 | Upload to GitHub Pages | Deploy report using peaceiris/actions-gh-pages |
| 8 | Publish Test Report | Publish JUnit XML results (optional) |

## Key Configuration Parameters

### GitHub Pages Deployment (peaceiris/actions-gh-pages@v3)

```yaml
- name: Upload Allure Report to GitHub Pages
  uses: peaceiris/actions-gh-pages@v3
  if: always()
  with:
    github_token: ${{ secrets.GITHUB_TOKEN }}    # Auto-generated token
    publish_dir: ./allure-report                 # Directory with Allure report
    user_name: 'github-actions[bot]'             # Commit author
    user_email: 'github-actions[bot]@users.noreply.github.com'
    commit_message: 'Deploy Allure Report'       # Commit message
    keep_files: true                             # Keep existing files in gh-pages branch
```

### Workflow Permissions

```yaml
permissions:
  contents: read              # Read repository contents
  pages: write                # Write to GitHub Pages
  id-token: write             # For OIDC token for deployment
```

## Accessing Your Allure Report

### Live Report URL
Once the workflow completes successfully, your Allure report will be available at:

```
https://<username>.github.io/<repository-name>/
```

### Example
If your repository is: `https://github.com/nikitha/playwrightPom_11May`

Your Allure report will be at: `https://nikitha.github.io/playwrightPom_11May/`

## Workflow Behavior

✅ **if: always()**
- Report upload runs even if tests fail
- Ensures reports are generated for both passing and failing test runs

✅ **keep_files: true**
- Preserves previously uploaded reports
- Maintains history of all test reports

✅ **Auto-deployment**
- Creates `gh-pages` branch automatically on first run
- Commits and pushes reports to `gh-pages` branch
- Uses `GITHUB_TOKEN` for authentication (no manual token needed)

## Common Issues & Solutions

### Issue 1: Report Not Updating
**Solution**: Ensure "keep_files: true" is set, then manually clear GitHub Pages cache by:
1. Disabling and re-enabling GitHub Pages in Settings
2. Or append `?v=<timestamp>` to URL to bypass cache

### Issue 2: Permission Denied Error
**Solution**: Check Settings → Actions → General → Workflow permissions
- Enable "Read and write permissions"

### Issue 3: gh-pages Branch Not Created
**Solution**: 
- First run the workflow and let it fail (to create branch)
- Then enable GitHub Pages pointing to `gh-pages` branch
- Push changes again

### Issue 4: Report Shows Old Results
**Solution**: Set `keep_files: true` to false if you want fresh reports only:
```yaml
keep_files: false
```

## Test Results Integration

The workflow also includes test reporting via `dorny/test-reporter`:
- Parses JUnit XML results
- Displays test results directly in GitHub UI
- Shows failures in PR checks

## Customization

### Run Tests on More Branches
```yaml
on:
  push:
    branches: [ main, develop, staging ]  # Add more branches
```

### Change Allure Version
```yaml
wget https://github.com/allure-framework/allure2/releases/download/2.20.1/allure-2.20.1.zip
```
(Replace version as needed)

### Modify Test Command
```yaml
run: pytest testPracticeAutomation/test_login.py -v --alluredir=allure-results
```
(Replace with your actual test command)

## Monitoring Workflow

### View Workflow Status
1. Go to your repository
2. Click **Actions** tab
3. See all workflow runs with status (✅ passed/❌ failed)
4. Click on a run to see detailed logs

### Debug Failed Runs
- Click on failed workflow run
- Expand any step to see console output
- Check "Install Allure Commandline" or "Run tests" steps for errors

## Benefits

✅ **Automated Testing** - Tests run on every push/PR
✅ **Historical Reports** - All reports available via GitHub Pages
✅ **Shareable** - Share reports link with team members
✅ **No Extra Tools** - Uses GitHub's native capabilities
✅ **Professional** - HTML reports with detailed metrics
✅ **Version Control** - Track test quality over time
✅ **CI/CD Integration** - Seamlessly integrates with GitHub workflow

## Additional Resources

- [peaceiris/actions-gh-pages](https://github.com/peaceiris/actions-gh-pages)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Allure Framework](https://docs.qameta.io/allure/)

---

**Ready to Deploy!** Your workflow is configured and ready to automatically deploy Allure reports to GitHub Pages.
