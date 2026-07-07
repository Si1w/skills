"""schema.py: template catalog and pydantic validation for weekly-report manifests.

TEMPLATES maps a stable template id to its slide index in the template pptx,
its purpose, and the meaning of every fillable shape id. This is the source of
truth: pick templates by id from here instead of re-inspecting the pptx.
"""

from pydantic import BaseModel, Field, model_validator

TEMPLATES = {
    "title": {
        "index": 0,
        "purpose": "Cover slide: report title, project name, researcher and date.",
        "text": {
            "85": "main title (default 'Weekly Research Update')",
            "86": "project name line, e.g. 'Project: X'",
            "87": "researcher and date line, e.g. 'Researcher: K | Date: 2026-07-07'",
        },
        "images": {},
        "optional": [],
    },
    "recap": {
        "index": 1,
        "purpose": "Context & recap: project overview (left) and last week's 1:1 recap (right).",
        "text": {
            "96": "motivation: why this research is being conducted",
            "97": "purpose: main goal or hypothesis",
            "98": "target venue (journal/conference)",
            "99": "deadline (DDL) for submission",
            "100": "recap: key discussion points from previous 1:1",
            "101": "recap: primary feedback/guidance from advisor",
            "102": "recap: action items set last session",
            "103": "recap: decisions on methodology or scope",
        },
        "images": {},
        "optional": ["104", "105", "106", "107", "108", "109", "110", "111"],  # arrow markers
    },
    "completed": {
        "index": 2,
        "purpose": "Completed tasks this week: three '[Category] description' rows.",
        "text": {
            "118": "completed item 1: '[Category] description'",
            "121": "completed item 2: '[Category] description'",
            "124": "completed item 3: '[Category] description'",
        },
        "images": {},
        "optional": ["117", "119", "120", "122", "123", "125"],  # row background shapes
    },
    "in-progress": {
        "index": 3,
        "purpose": "Ongoing work: three '[Active Task] status' rows.",
        "text": {
            "135": "active task 1: description and current status",
            "138": "active task 2: description and current status",
            "141": "active task 3: description and current status",
        },
        "images": {},
        "optional": ["134", "136", "137", "139", "140", "142"],  # row background shapes
    },
    "results": {
        "index": 4,
        "purpose": "One figure/table with explanation and takeaway. Repeat once per figure.",
        "text": {
            "154": "explanation: methodology behind the figure",
            "155": "explanation: variables/axes/conditions shown",
            "156": "takeaway: core insight from this result",
            "157": "takeaway: impact on project direction / next steps",
        },
        "images": {"151": "the figure/table image (landscape frame on the left)"},
        "optional": ["158", "159", "160", "161", "162"],  # sample chart + arrow markers
    },
    "results-text": {
        "index": 5,
        "purpose": "Text-only results: full-page explanation/takeaway card, for results without a figure or table.",
        "text": {"172": "explanation and takeaway message (multi-line; keep the leading arrow style)"},
        "images": {},
        "optional": [],
    },
    "results-big-figure": {
        "index": 6,
        "purpose": "Full-width large figure (e.g. wide/landscape plots or tables rendered to PNG) with a caption line.",
        "text": {"178": "figure/table caption, e.g. 'Figure 1.1: ...'"},
        "images": {"figure": "the large figure; replaces the sample chart, fitted to the full-width card"},
        # sample chart shapes cleared when "figure" is set; card background 180 is kept
        "figure_slot": {"region": [1.0, 2.15, 11.33, 4.45], "clear": ["181", "187", "188", "189", "190", "197", "204", "205"]},
        "optional": [],
    },
    "blockers": {
        "index": 7,
        "purpose": "Support needed & blockers: technical, conceptual, resource columns.",
        "text": {
            "219": "technical/methodological blockers",
            "221": "conceptual/literature questions needing advice",
            "223": "resource/administrative requests",
        },
        "images": {},
        "optional": [],
    },
    "plans": {
        "index": 8,
        "purpose": "Plans & timeline: next week, this month, long-term milestone, target DDL.",
        "text": {
            "234": "short term: goals before next 1:1",
            "236": "short term: goals within 3-4 weeks",
            "238": "long term: major milestone before finalizing",
            "240": "target DDL for submission/review",
        },
        "images": {},
        "optional": ["232", "241", "242", "243", "244"],  # timeline decorations
    },
    "next-week": {
        "index": 9,
        "purpose": "Closing divider: 'Plan for the Next Week'.",
        "text": {"250": "divider title"},
        "images": {},
        "optional": [],
    },
}


class SlideSpec(BaseModel):
    template: str
    text: dict[str, str] = Field(default_factory=dict)
    images: dict[str, str] = Field(default_factory=dict)
    delete: list[str] = Field(default_factory=list)

    @model_validator(mode="after")
    def check_against_catalog(self):
        if self.template not in TEMPLATES:
            raise ValueError(f"unknown template {self.template!r}; choose from {list(TEMPLATES)}")
        cat = TEMPLATES[self.template]
        editable = set(cat["text"]) | set(cat["images"]) | set(cat["optional"])
        for sid in self.text:
            if sid not in cat["text"]:
                raise ValueError(f"{self.template}: shape {sid} is not a text field; fields: {cat['text']}")
        for sid in self.images:
            if sid not in cat["images"]:
                raise ValueError(f"{self.template}: shape {sid} is not an image slot; slots: {cat['images']}")
        for sid in self.delete:
            if sid not in editable:
                raise ValueError(f"{self.template}: shape {sid} is not deletable; allowed: {sorted(editable)}")
        return self


class Manifest(BaseModel):
    slides: list[SlideSpec] = Field(min_length=1)
