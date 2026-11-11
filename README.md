# >_ RAID · Securinets ENIT

A team repository for the Git Quest season 2 raid. You'll work like a real team:
`main` is protected, every change goes through a reviewed pull request.

## Captain: set up (stage 1)

1. **Use this template** → Create a new repository → your account · `raid-<team-name>` · **Public**.
2. Edit `TEAM.md` (directly on `main`, the last direct commit ever): team name + members.
3. Settings → **Collaborators** → add each member. Members accept the invitation.
4. Settings → **Rules** → **Rulesets** → New branch ruleset `protect-main`:
   Active · Include default branch · Restrict deletions · Block force pushes ·
   **Require a pull request before merging** (1 approval).
5. On **securinets-enit/git-quest-2**: Issues → New issue → **Start the Raid** → paste this repo's link.

## Files

| File | Who edits it | How |
|---|---|---|
| `TEAM.md` | captain | once, before the ruleset |
| `members/<login>.md` | each member | through a pull request |
| `mission.md` | everyone | through pull requests (stage 4: a collision!) |

The **validate** workflow checks every pull request.
