# Keyboard shortcuts

Press ++question++ inside the annotation workspace to bring up this sheet in the
app.

## Tools

| Key | Tool |
|---|---|
| ++v++ | Select & edit |
| ++p++ | Point |
| ++b++ | Bounding box |
| ++g++ | Polygon |
| ++f++ | Freehand |
| ++m++ | Brush / mask — **not available in this build** |
| ++h++ | Pan |
| ++z++ | Zoom |
| ++a++ | On prompt: cycle Nothing → Run AI → Add |

## Actions

| Key | Action |
|---|---|
| ++enter++ | Run AI on the placed prompts, or accept |
| ++shift+enter++ | Add the drawn outlines as objects |
| ++1++ | Run prompted segmentation |
| ++2++ | Suggest similar instances |
| ++3++ | Run instance segmentation |
| ++l++ | Open the label picker |
| ++e++ | Edit the selected contour |
| ++r++ | Reject (review mode) |
| ++backspace++ | Remove last prompt, or delete the selection |
| ++esc++ | Clear the selection, leave focus mode, or cancel a calibration measurement |

## View

| Key | Action |
|---|---|
| ++left++ ++right++ | Previous / next image |
| ++plus++ ++minus++ | Zoom in / out |
| ++0++ | Fit to screen |
| ++alt+1++ | Toggle the tool-options drawer |
| ++alt+2++ | Toggle the side panel |
| ++t++ | Label chips — all / selected only / off |
| ++space++ | Hold to pan |
| ++question++ | This sheet |

## History

| Key | Action |
|---|---|
| ++cmd+z++ | Undo — the last prompt, or your last annotation action |
| ++cmd+shift+z++ | Redo the last undone step |
| ++cmd+shift+c++ | Clear all prompts |

!!! info "One key, two undo stacks"
    ++cmd+z++ undoes prompts on the canvas first, and only then reaches back into
    your annotation history. The difference is invisible otherwise, which is why
    it is spelled out here.

## What happens when a prompt is placed

The **prompt action** control decides what a placed prompt does. ++a++ cycles
through the three settings.

| Setting | Behaviour |
|---|---|
| **Nothing** | Prompts stay on the canvas. Run them through the AI or add them yourself, whenever you are ready. |
| **Run AI** | Every prompt runs through the model as soon as it is placed. |
| **Add** | A polygon or freehand outline is added as an object as soon as you close it. Points and boxes are not offered. |
