# Final release and branch-protection steps

The GitHub integration used for the repairs cannot create Git annotated tags, change repository rulesets, or delete merged branches. Perform these remaining operations from your own machine with write access. **Do not force-push or move the existing tags v1.0.0 and v1.1.0.**

## 1. Fetch and verify

```bash
git clone https://github.com/son107306/it3180-202416339-aims.git
cd it3180-202416339-aims
git fetch --all --tags --prune
python main.py
python -m unittest discover -s tests -v
git branch -r
git tag -n
```

## 2. Create missing immutable annotated tags

Each tag points to the correct milestone. `v1.0.1` points to the restored Lab 04 baseline *before* the non-finite-price hotfix, which is tagged `v1.0.2`.

```bash
git tag -a v0.1.0 origin/release/lab01 -m "IT3180 Lab 01 baseline"
git tag -a v0.2.0 origin/release/lab02 -m "IT3180 Lab 02 baseline"
git tag -a v0.3.0 origin/release/lab03 -m "IT3180 Lab 03 baseline"
git tag -a v1.0.1 aa5c0a6600966a81ff10b095ec6697bb43c7128f -m "Restored AIMS-mini 1.0.1 baseline"
git tag -a v1.0.2 origin/release/lab04 -m "AIMS-mini 1.0.2 validated hotfix"
git tag -a v1.1.1 origin/release/lab05 -m "AIMS-mini 1.1.1 corrected Lab 05 release"
git push origin v0.1.0 v0.2.0 v0.3.0 v1.0.1 v1.0.2 v1.1.1
```

**Before running:** Confirm all these tags do not already exist (`git tag -l`) and `origin/release/lab05` contains the 1.1.1 version bump. Annotated tags should only be created once, after test verification. The historical tags v1.0.0 and v1.1.0 remain unchanged.

## 3. GitHub Release

GitHub → Releases → Draft a new release. Choose the **existing** tag `v1.0.2`, target release/lab04; copy [1.0.2] notes from CHANGELOG. Repeat for `v1.1.1`, target release/lab05. Do not reassign the old v1.0.0/v1.1.0 releases.

## 4. Branch protection

GitHub → Settings → Rules → Rulesets (or Branches):
- Target `master` and `release/*`.
- Require pull request before merging.
- Require status check `test` after CI publishes it.
- Disable bypass where available and block force-push/deletion.
- For solo work, approval count 0; for a partner, 1. Do not claim an approval that never occurred.

## 5. Remaining practical evidence

- A partner must actually review a PR and use Changes requested then Approve (the PR author cannot approve their own work).
- On the local clone, practice and record `git mv`, restore/staged restore, amend on an **unpublished** commit, reset/reflog on unpublished scratch branch, and `git cherry-pick -x` in a scratch copy if the rubric demands terminal evidence.
- Confirm CI is green on master and all release refs; attach screenshots from genuine execution as necessary.
- Delete short-lived source branches **after their PR is merged** via GitHub's PR UI; preserve `master` and `release/lab01..05`.
