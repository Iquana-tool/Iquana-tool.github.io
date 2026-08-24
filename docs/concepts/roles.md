# Roles and permissions

Access control has two independent levels.

- **Global role** — stored on the account, answers *"what may this account do to
  the platform?"* Create datasets at all, manage other users, touch the model
  registry.
- **Dataset role** — stored on the membership row, answers *"what may this
  account do to **this** dataset?"*

Datasets are IQUANA's unit of governance, so nearly every permission lives at the
dataset level. An account can hold a different role in every dataset it belongs
to.

## Global roles

| Global role | May |
|---|---|
| **admin** | everything, platform-wide — user management, global roles, the model registry |
| **member** | create datasets of their own |
| **guest** | nothing globally; can only work inside datasets they were invited to |

## Dataset roles

Ranked from least to most privileged. **Each role includes everything the role
above it in this table can do.**

### viewer

Read-only. Sees the dataset, its images, its label space and its annotations.

### annotator

Everything a viewer can do, plus:

- create annotations, and edit or delete **their own**
- submit masks
- use interactive AI segmentation

### reviewer

Everything an annotator can do, plus:

- edit **any** annotation, not only their own
- reopen and delete masks
- approve, reject and revoke reviews; purge unreviewed items
- export annotations and quantification results

### curator

Everything a reviewer can do, plus:

- update dataset settings; upload and delete images
- **write image metadata**
- **set the pixel scale and other calibrations**
- manage the label space
- run batch inference and training
- export images
- list members and create invites

### owner

Everything a curator can do, plus:

- delete the dataset, and transfer its ownership
- grant and revoke membership
- revoke invites

## Why calibration and metadata sit at curator, not annotator

Two permissions are deliberately held back from people doing annotation work:

!!! info "Image metadata"
    Metadata defines the subgroups a dataset is later compared across. An
    annotator retagging images would silently redraw the groups someone else's
    analysis is built on.

!!! info "Calibration and pixel scale"
    Changing the scale silently rescales **every quantification number in the
    dataset**. Calibration changes what the stored measurements *mean*, not what
    is annotated — which is curation, not annotation.

## Per-member exceptions

A membership row can additionally carry extra or denied permissions, so one
collaborator can be given — or refused — a single capability without inventing a
new role for them.

## Invites and privilege

Redeeming an invite never *downgrades* an existing member: roles are ranked, and
the higher of the two is kept.

<div class="iq-shot-todo">
  <span><strong>Recording slot — <code>access-and-roles</code></strong><br>
  Dataset access page → create an invite → assign a role → the same surface seen as
  an annotator vs. a curator.<br>
  12–16 s · dark theme · 1280×800</span>
</div>

!!! note "The first account"
    The first account created on an installation becomes the platform
    administrator, whether or not self-registration is enabled. See
    [Configuration](../getting-started/configuration.md#identifying-your-instance).
