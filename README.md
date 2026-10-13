![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# Attribute Reset Tool for Autodesk Maya

---

## Overview

**Attribute Reset** is a lightweight Autodesk Maya utility that helps animators and rigging artists quickly restore controller attributes to their **defined default values**.

Instead of manually changing each value in the Channel Box, artists can reset multiple selected controllers at once or highlight only the specific attributes they want to restore.

The tool installs directly onto the current Maya shelf through a simple **drag-and-drop Python installer**, making it convenient for everyday animation and rigging workflows.

> ⚠️ This tool is intended for personal and production workflow use. Test it on your rigs before integrating it into a shared pipeline.

---

## Features

- Drag-and-drop Python installation directly into the Maya viewport
- Automatic shelf button creation on the currently active shelf
- Reset multiple selected objects or controllers in one operation
- Reset only the attributes highlighted in Maya's Channel Box
- Restore values using each attribute's stored default, including custom rig attributes where a default is defined
- Handle supported numeric, enum, string, and compound attribute types
- Skip locked attributes and report attributes that cannot be reset
- Lightweight implementation using Maya's built-in `maya.cmds` and `maya.mel`

---

## Workflow Concept

### Reset All Eligible Attributes

Select one or more controllers and click the **Default** shelf button **without highlighting any Channel Box attributes**.

The tool checks each selected object for eligible **keyable and unlocked attributes** and attempts to restore them to their stored defaults.

This is useful when artists need to:

- return a character controller to its default pose
- clear experimental controller adjustments
- reset several controls before starting a new pose
- restore custom rig settings to their default values

---

### Reset Selected Channel Box Attributes

For more precise control, highlight one or more attributes in Maya's **Channel Box** before clicking the shelf button.

Only the highlighted attribute names are considered for the selected objects. Attributes that do not exist on a particular selected object are skipped.

For example:

- Select a controller
- Highlight **Translate X** and **Translate Y** in the Channel Box
- Click **Default**
- The tool attempts to restore those channels to their defined defaults, leaving other channels untouched

This is especially useful for resetting individual translation, rotation, scale, or custom rig attributes without affecting the rest of a pose.

---

### Default Value Detection

The tool queries each attribute's stored default value rather than assuming every attribute should become `0`.

For example, a typical Maya transform may have:

| Attribute | Typical Default |
| --- | ---: |
| Translate X / Y / Z | `0` |
| Rotate X / Y / Z | `0` |
| Scale X / Y / Z | `1` |
| Custom attributes | Their defined defaults |

Actual results depend on how each attribute was created and whether Maya exposes a usable default value.

---

### Attribute Safety Checks

During a reset, the tool:

- ignores attributes that do not exist on a selected object
- skips locked attributes
- skips attributes without a reported default value
- displays a warning when an attribute cannot be modified

> **Note:** This is a value-reset utility, not an animation-curve cleanup tool. It does not remove keyframes, disconnect incoming connections, or bake animation. Driven or connected attributes may not be editable and can be skipped with warnings.

---

## Installation

1. Open **Autodesk Maya**.
2. Select the shelf tab where you want to install the tool.
3. Drag and drop `AttributeReset_Install.py` into the Maya viewport.
4. A shelf button labelled **Default** will be created automatically.
5. Click **Default** whenever you want to reset selected controller attributes.

The installer uses Maya's native Python drag-and-drop handler and does not require external Python packages.

**Compatibility:** Designed for Maya versions that support Python file drag-and-drop installation. The script uses basic Maya commands, but compatibility has not been verified across every Maya release.

---

## Usage

### Option 1 — Reset Controller Attributes

1. Select one or more controllers or objects in Maya.
2. Make sure no individual attributes are highlighted in the Channel Box.
3. Click the **Default** shelf button.
4. The tool attempts to restore eligible keyable, unlocked attributes to their default values.

### Option 2 — Reset Specific Attributes

1. Select one or more controllers or objects in Maya.
2. Highlight the desired attribute(s) in the Channel Box.
3. Click the **Default** shelf button.
4. Only the highlighted attribute names are processed for the selected objects.

---

## Notes & Limitations

- **No selection:** The tool requires at least one selected object.
- **Locked channels:** Locked attributes are intentionally skipped.
- **Connected channels:** Incoming connections can prevent attributes from being set.
- **Custom attributes:** Defaults must be defined and queryable by Maya.
- **Channel Box scope:** Highlighted attribute names are applied across the selected objects where those attributes exist.
- **Existing animation:** Resetting current values does not erase animation keys or incoming connections.
- **Shelf installation:** The button is added to the currently active shelf; the installer is not a separate UI window.

---

## Feedback & Contributions

This is a lightweight personal workflow utility intended to help artists reduce repetitive Channel Box operations.

Feedback, production suggestions, bug reports, and improvement ideas are welcome.

If you encounter issues with a particular Maya version, rig setup, or attribute type, feel free to open an issue or share a reproducible example.

---

## License

Provided **as-is** for personal and educational use. No separate license file is included with this README.
