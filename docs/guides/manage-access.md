# Manage access

**You need:** `curator` to list members and create invites; `owner` to grant or
revoke membership and revoke invites.

Read [Roles and permissions](../concepts/roles.md) first — the role you hand
someone is the whole decision.

## Steps

1. Open the dataset's access page.
2. **Create an invite** and choose the role it grants.
3. Send the invite link to the person.
4. They redeem it and appear as a member.

<div class="iq-shot-todo">
  <span><strong>Recording slot — <code>access-and-roles</code></strong><br>
  Access page → create an invite → assign a role → the same surface as annotator
  vs. curator.<br>
  12–16 s · dark theme · 1280×800</span>
</div>

## Choosing a role

| Give them | If they should |
|---|---|
| **viewer** | look, and nothing else |
| **annotator** | annotate, and edit only their own work |
| **reviewer** | edit anyone's annotations, run review, export measurements |
| **curator** | also upload images, manage labels, calibrate, run inference and training |
| **owner** | also delete the dataset, and manage membership |

!!! tip "Calibration and metadata are curator-level for a reason"
    Both silently change what existing measurements mean. If someone only needs
    to annotate, `annotator` is the correct answer even when they ask for more.

## Exceptions without new roles

A membership can carry extra or denied permissions individually, so one
collaborator can be given — or refused — a single capability without inventing a
role for them.

## Invites never downgrade

Redeeming an invite keeps the higher of the two roles, so re-inviting an existing
member cannot accidentally demote them.

## Platform-level accounts

Creating accounts, setting global roles and deciding whether self-registration is
allowed are platform concerns, not dataset ones. See
[Configuration](../getting-started/configuration.md#identifying-your-instance).
