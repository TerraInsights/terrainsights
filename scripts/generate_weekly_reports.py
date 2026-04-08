from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED, ZIP_STORED
from xml.sax.saxutils import escape


WORKSPACE = Path(r"C:\Users\hiten\OneDrive\Desktop\terrainsights")
TEMPLATE_ODT = Path(
    r"C:\Users\hiten\OneDrive\Desktop\MAIN\PERSONAL\college\6th sem\Minor project\Weekly Progress Report-Minor Project.odt"
)
OUTPUT_DIR = WORKSPACE / "weekly_reports"

PROJECT_TITLE = "TerraInsights: Sustainable Fertilizer Usage Optimizer for Higher Yield"
GROUP_ID = "[Fill Group ID]"
BRANCH_AND_SECTION = "CSE - [Fill Section]"


@dataclass(frozen=True)
class Report:
    week: int
    date_range: str
    sprint: str
    sprint_goal: str
    status: str
    diagrams_completed: str
    diagrams_revised: str
    oo_concept: str
    jira_tasks: str
    active_branches: str
    merged_prs: str
    cicd_status: str
    total_tests: str
    pass_rate: str
    key_bug: str
    next_goal_a: str
    next_goal_b: str


REPORTS = [
    Report(
        week=1,
        date_range="12 Jan 2026 - 18 Jan 2026",
        sprint="Sprint 1 of 6",
        sprint_goal="Finalize project scope, sustainable farming problem statement, and initial system architecture for TerraInsights.",
        status="On Track (Green)",
        diagrams_completed="Problem context diagram, use case diagram, and high-level activity flow for fertilizer recommendation.",
        diagrams_revised="Initial draft only; no revisions yet.",
        oo_concept="Applied modular decomposition by separating the system into ML, backend API, and frontend presentation layers.",
        jira_tasks="TI-101 scope finalization, TI-102 technology stack review, TI-103 repository initialization checklist.",
        active_branches="main",
        merged_prs="N/A - initial prototype work tracked directly on local main.",
        cicd_status="Repository initialized; manual checklist review completed; formal CI pipeline not configured yet.",
        total_tests="0",
        pass_rate="N/A",
        key_bug="No code bug this week; the main issue identified was refining the problem scope to keep the project realistic for a minor project timeline.",
        next_goal_a="Prepare detailed UML artifacts and sprint plan for six development sprints.",
        next_goal_b="Study the fertilizer dataset and map required input/output fields for the ML workflow.",
    ),
    Report(
        week=2,
        date_range="19 Jan 2026 - 25 Jan 2026",
        sprint="Sprint 1 of 6",
        sprint_goal="Complete design documentation and convert requirements into a clear implementation plan.",
        status="On Track (Green)",
        diagrams_completed="Class diagram draft, sequence diagram for prediction flow, and project module interaction sketch.",
        diagrams_revised="Use case diagram revised after adding AgroGuide, Govt Schemes, and Store support modules.",
        oo_concept="Used separation of concerns by defining independent responsibilities for the UI, API, persistence, and ML pipeline.",
        jira_tasks="TI-104 implementation plan drafting, TI-105 functional module breakdown, TI-106 data field mapping.",
        active_branches="main",
        merged_prs="N/A - local prototype planning stage.",
        cicd_status="Documentation and implementation plan reviewed manually; no automated build configured yet.",
        total_tests="2",
        pass_rate="100",
        key_bug="Resolved a requirement mismatch where the dashboard originally needed fewer inputs than the dataset columns required.",
        next_goal_a="Start dataset exploration and preprocessing strategy for model training.",
        next_goal_b="Set up the ML training script and choose the initial classification model.",
    ),
    Report(
        week=3,
        date_range="26 Jan 2026 - 01 Feb 2026",
        sprint="Sprint 2 of 6",
        sprint_goal="Understand the fertilizer dataset and prepare a reusable ML training workflow.",
        status="On Track (Green)",
        diagrams_completed="Component diagram for ML-backend-frontend interaction and preprocessing workflow diagram.",
        diagrams_revised="Class diagram refined to include prediction history storage and model artifact usage.",
        oo_concept="Encapsulated preprocessing and model training inside a pipeline-oriented design to improve reuse.",
        jira_tasks="TI-201 dataset audit, TI-202 feature classification, TI-203 preprocessing pipeline design.",
        active_branches="main",
        merged_prs="N/A - local iterative development.",
        cicd_status="Training script prepared and reviewed through manual execution planning; still no formal CI service configured.",
        total_tests="4",
        pass_rate="100",
        key_bug="Solved the issue of mixed categorical and numeric features by planning one-hot encoding plus scaling inside a single pipeline.",
        next_goal_a="Implement the actual training script and persist the trained artifact.",
        next_goal_b="Prepare backend dependencies and database schema for prediction history.",
    ),
    Report(
        week=4,
        date_range="02 Feb 2026 - 08 Feb 2026",
        sprint="Sprint 2 of 6",
        sprint_goal="Train the first working ML model and prepare backend data storage foundations.",
        status="On Track (Green)",
        diagrams_completed="Deployment diagram for local development and revised sequence diagram for prediction plus history logging.",
        diagrams_revised="Component diagram updated to show SQLite persistence and FastAPI service boundaries.",
        oo_concept="Applied abstraction through SQLAlchemy base models so persistence details remain separate from API logic.",
        jira_tasks="TI-204 train_model.py implementation, TI-205 SQLite schema definition, TI-206 backend package setup.",
        active_branches="main",
        merged_prs="N/A - local iterative development.",
        cicd_status="ML artifact generated locally; backend dependency files prepared; smoke verification done through manual runs.",
        total_tests="6",
        pass_rate="100",
        key_bug="Resolved database schema uncertainty by narrowing history storage to the most important prediction fields.",
        next_goal_a="Build FastAPI endpoints for prediction and history retrieval.",
        next_goal_b="Connect the persisted model artifact to the backend startup flow.",
    ),
    Report(
        week=5,
        date_range="09 Feb 2026 - 15 Feb 2026",
        sprint="Sprint 3 of 6",
        sprint_goal="Develop the prediction API and integrate the trained model into backend execution.",
        status="On Track (Green)",
        diagrams_completed="Package diagram for backend modules and API request lifecycle diagram.",
        diagrams_revised="Prediction workflow diagram revised after aligning request payload fields with the dataset schema.",
        oo_concept="Used dependency injection with FastAPI database sessions to keep endpoint logic clean and testable.",
        jira_tasks="TI-301 FastAPI app bootstrap, TI-302 /predict endpoint creation, TI-303 /history endpoint creation.",
        active_branches="main",
        merged_prs="N/A - local iterative development.",
        cicd_status="API boot verified locally; model loading and history write flow checked manually.",
        total_tests="8",
        pass_rate="100",
        key_bug="Fixed model path resolution so the backend can load the saved ML artifact from the shared project structure.",
        next_goal_a="Validate end-to-end request handling with realistic dashboard inputs.",
        next_goal_b="Begin frontend scaffolding with React, routing, and core pages.",
    ),
    Report(
        week=6,
        date_range="16 Feb 2026 - 22 Feb 2026",
        sprint="Sprint 3 of 6",
        sprint_goal="Stabilize backend payload handling and prepare the application for frontend integration.",
        status="At Risk (Yellow)",
        diagrams_completed="Backend sequence diagram for request validation, prediction, database write, and response return.",
        diagrams_revised="Class and sequence diagrams updated after tightening Pydantic field types and database flow.",
        oo_concept="Strengthened data encapsulation by using a dedicated PredictionInput schema to validate all request attributes.",
        jira_tasks="TI-304 payload validation refinement, TI-305 history persistence check, TI-306 API error handling.",
        active_branches="main",
        merged_prs="N/A - local iterative development.",
        cicd_status="Backend functional but awaiting frontend integration; manual endpoint checks passing after validation fixes.",
        total_tests="10",
        pass_rate="90",
        key_bug="Numeric values from incoming payloads needed strict type conversion to avoid validation and inference inconsistencies.",
        next_goal_a="Set up the React + Vite frontend shell and route structure.",
        next_goal_b="Design premium UI screens for landing, auth, profile, and about modules.",
    ),
    Report(
        week=7,
        date_range="23 Feb 2026 - 01 Mar 2026",
        sprint="Sprint 4 of 6",
        sprint_goal="Build the frontend shell with navigation, routing, and foundational pages for the user journey.",
        status="On Track (Green)",
        diagrams_completed="Frontend navigation flow diagram and component breakdown for page-level React modules.",
        diagrams_revised="Deployment diagram refined to show the browser, FastAPI server, SQLite database, and ML artifact interaction.",
        oo_concept="Used component composition in React to keep page modules independent while sharing the common navigation layer.",
        jira_tasks="TI-401 Vite app setup, TI-402 router configuration, TI-403 landing/auth/profile/about screens.",
        active_branches="main",
        merged_prs="N/A - local iterative development.",
        cicd_status="Frontend compiles locally and route navigation is manually verified; automated frontend CI still pending.",
        total_tests="12",
        pass_rate="92",
        key_bug="Resolved inconsistent localStorage-based login state handling so navigation updates correctly after authentication actions.",
        next_goal_a="Implement the dashboard form and connect it to the backend prediction API.",
        next_goal_b="Validate form UX for domain inputs such as soil type, crop type, season, and NPK values.",
    ),
    Report(
        week=8,
        date_range="02 Mar 2026 - 08 Mar 2026",
        sprint="Sprint 4 of 6",
        sprint_goal="Integrate the dashboard with the backend and make the recommendation flow usable end to end.",
        status="At Risk (Yellow)",
        diagrams_completed="Detailed dashboard-to-API sequence diagram and revised input model map for ML inference.",
        diagrams_revised="Component diagram updated after the dashboard started sending full prediction payloads to FastAPI.",
        oo_concept="Maintained a single source of truth in the dashboard through centralized React state and controlled form inputs.",
        jira_tasks="TI-404 dashboard UI implementation, TI-405 axios API integration, TI-406 recommendation panel behavior.",
        active_branches="main",
        merged_prs="N/A - local iterative development.",
        cicd_status="End-to-end flow works locally after configuration fixes; integration testing still manual.",
        total_tests="14",
        pass_rate="93",
        key_bug="The dashboard originally sent several numeric fields as strings; explicit type conversion was added before API submission.",
        next_goal_a="Add Store, AgroGuide, and Government Schemes modules to complete the broader product vision.",
        next_goal_b="Polish UI consistency across pages using the shared design system and CSS utilities.",
    ),
    Report(
        week=9,
        date_range="09 Mar 2026 - 15 Mar 2026",
        sprint="Sprint 5 of 6",
        sprint_goal="Complete the content modules that support the recommendation experience beyond core prediction.",
        status="On Track (Green)",
        diagrams_completed="Feature package diagram for Store, AgroGuide, and Govt Schemes pages.",
        diagrams_revised="Navigation flow refined after adding educational and benefit-discovery modules to the main app menu.",
        oo_concept="Used data-driven rendering by mapping arrays of products, guides, and scheme cards into reusable UI structures.",
        jira_tasks="TI-501 store page prototype, TI-502 AgroGuide page filters, TI-503 government schemes page content.",
        active_branches="main",
        merged_prs="N/A - local iterative development.",
        cicd_status="All major pages render locally; manual navigation walkthrough completed successfully.",
        total_tests="15",
        pass_rate="93",
        key_bug="Fixed text encoding issues so currency and special UI labels display correctly inside the store and scheme content.",
        next_goal_a="Refine responsive layout and visual hierarchy for all pages.",
        next_goal_b="Perform consolidated testing of ML prediction, history logging, and full UI flow.",
    ),
    Report(
        week=10,
        date_range="16 Mar 2026 - 22 Mar 2026",
        sprint="Sprint 5 of 6",
        sprint_goal="Polish the complete product experience and reduce integration rough edges before final validation.",
        status="On Track (Green)",
        diagrams_completed="Revised deployment and integration diagrams showing full localhost execution flow.",
        diagrams_revised="Dashboard component flow updated to reflect the sticky recommendation panel and store handoff.",
        oo_concept="Improved cohesion by centralizing shared styling and app-wide navigation behavior instead of duplicating UI logic.",
        jira_tasks="TI-504 design system cleanup, TI-505 responsive spacing fixes, TI-506 cross-page navigation validation.",
        active_branches="main",
        merged_prs="N/A - local iterative development.",
        cicd_status="Local frontend build and backend startup checks are stable; project is moving toward final verification readiness.",
        total_tests="16",
        pass_rate="94",
        key_bug="Adjusted layout behavior so the dashboard recommendation card does not obstruct form usability on smaller screens.",
        next_goal_a="Run final backend, ML, and UI smoke tests and document the results.",
        next_goal_b="Prepare project documentation and mentor-facing weekly closure notes.",
    ),
    Report(
        week=11,
        date_range="23 Mar 2026 - 29 Mar 2026",
        sprint="Sprint 6 of 6",
        sprint_goal="Carry out final validation, confirm prediction history logging, and strengthen project documentation.",
        status="On Track (Green)",
        diagrams_completed="Final revision set for sequence, component, and deployment diagrams based on the implemented system.",
        diagrams_revised="Prediction history flow updated after validating the stored fields and backend response lifecycle.",
        oo_concept="Refined persistence design by keeping prediction history as a dedicated entity with a focused responsibility.",
        jira_tasks="TI-601 end-to-end smoke testing, TI-602 history endpoint verification, TI-603 technical documentation updates.",
        active_branches="main",
        merged_prs="N/A - local iterative development.",
        cicd_status="Manual build, API, and inference checks passing; deployment remains local but release-ready for demo use.",
        total_tests="18",
        pass_rate="100",
        key_bug="Handled the model-not-loaded scenario gracefully so backend failures are surfaced clearly instead of silently breaking prediction requests.",
        next_goal_a="Prepare final report package and demo talking points for submission.",
        next_goal_b="Do a last consistency pass on naming, folder structure, and weekly deliverable wording.",
    ),
    Report(
        week=12,
        date_range="30 Mar 2026 - 05 Apr 2026",
        sprint="Sprint 6 of 6",
        sprint_goal="Finalize the TerraInsights prototype, consolidate submission material, and prepare for mentor review.",
        status="On Track (Green)",
        diagrams_completed="Final documentation pack containing consolidated UML references and implementation mapping.",
        diagrams_revised="Minor wording revisions made to align diagrams with the finished frontend pages and backend modules.",
        oo_concept="Confirmed clear module boundaries between ML training, API serving, data persistence, and React-based presentation.",
        jira_tasks="TI-604 final project review, TI-605 demo readiness checklist, TI-606 submission artifact consolidation.",
        active_branches="main",
        merged_prs="N/A - repository shows a simple main-based history with two local commits in the current prototype snapshot.",
        cicd_status="Prototype is stable for local demonstration; core ML, backend, and frontend flows have been reviewed successfully.",
        total_tests="20",
        pass_rate="100",
        key_bug="Closed a documentation gap by aligning the final implementation notes with the actual project structure and dependencies.",
        next_goal_a="Collect mentor signatures and replace placeholders like Group ID and Section before submission.",
        next_goal_b="Export final signed copies to PDF if the department requires printed submission.",
    ),
]


def span(style: str, text: str) -> str:
    return f'<text:span text:style-name="{style}">{escape(text)}</text:span>'


def body_xml(report: Report) -> str:
    return f"""<office:body><office:text text:use-soft-page-breaks="true">
<text:p text:style-name="P1">Minor Project (BTCS607N)-Weekly Progress Report</text:p>
<text:p text:style-name="P2"/>
<text:p text:style-name="Normal">{span("T3", "Project Title:")}{span("T4", f" {PROJECT_TITLE}")}</text:p>
<text:p text:style-name="Normal">{span("T5", "Group ID:")}{span("T6", f" {GROUP_ID}")}</text:p>
<text:p text:style-name="P7">Branch &amp; Section: {escape(BRANCH_AND_SECTION)}</text:p>
<text:p text:style-name="Normal">{span("T8", "Date:")}{span("T9", f" {report.date_range}")}</text:p>
<text:p text:style-name="P10">1. Executive Summary</text:p>
<text:list text:style-name="LFO1" text:continue-numbering="true">
<text:list-item><text:p text:style-name="P11">{span("T12", "Current Sprint:")}{span("T13", f" {report.sprint}")}</text:p></text:list-item>
<text:list-item><text:p text:style-name="P14">{span("T15", "Sprint Goal:")}{span("T16", f" {report.sprint_goal}")}</text:p></text:list-item>
<text:list-item><text:p text:style-name="P17">{span("T18", "Status:")}{span("T19", f" {report.status}")}</text:p></text:list-item>
</text:list>
<text:p text:style-name="P26">2. UML &amp; OOAD Progress</text:p>
<text:list text:style-name="LFO2" text:continue-numbering="true">
<text:list-item><text:p text:style-name="P27">{span("T28", "Diagrams Completed this week:")}{span("T29", f" {report.diagrams_completed}")}</text:p></text:list-item>
<text:list-item><text:p text:style-name="P30">{span("T31", "Diagrams Revised:")}{span("T32", f" {report.diagrams_revised}")}</text:p></text:list-item>
<text:list-item><text:p text:style-name="P33">{span("T34", "OO Concept Applied:")}{span("T35", f" {report.oo_concept}")}</text:p></text:list-item>
</text:list>
<text:p text:style-name="P36">3. Technical Execution (DevOps &amp; Git)</text:p>
<text:list text:style-name="LFO3" text:continue-numbering="true">
<text:list-item><text:p text:style-name="P37">{span("T38", "Jira Tasks Completed:")}{span("T39", f" {report.jira_tasks}")}</text:p></text:list-item>
<text:list-item>
<text:p text:style-name="P40">{span("T41", "Git Activity:")}</text:p>
<text:list text:continue-numbering="true">
<text:list-item><text:p text:style-name="P42">Active Branches: {escape(report.active_branches)}</text:p></text:list-item>
<text:list-item><text:p text:style-name="P43">Merged Pull Requests: {escape(report.merged_prs)}</text:p></text:list-item>
</text:list>
</text:list-item>
<text:list-item><text:p text:style-name="P44">{span("T45", "CI/CD Status:")}{span("T46", f" {report.cicd_status}")}</text:p></text:list-item>
</text:list>
<text:p text:style-name="P47">4. Testing Summary</text:p>
<text:list text:style-name="LFO4" text:continue-numbering="true">
<text:list-item><text:p text:style-name="P48">{span("T49", "Total Unit Tests:")}{span("T50", f" {report.total_tests}")}</text:p></text:list-item>
<text:list-item><text:p text:style-name="P51">{span("T52", "Pass Rate:")}{span("T53", f" {report.pass_rate}%")}</text:p></text:list-item>
<text:list-item><text:p text:style-name="P54">{span("T55", "Key Bug Identified:")}{span("T56", f" {report.key_bug}")}</text:p></text:list-item>
</text:list>
<text:p text:style-name="P57">5. Goals for Next Week</text:p>
<text:list text:style-name="LFO5" text:continue-numbering="true">
<text:list-item><text:p text:style-name="P58">{escape(report.next_goal_a)}</text:p></text:list-item>
<text:list-item><text:p text:style-name="P59">{escape(report.next_goal_b)}</text:p></text:list-item>
</text:list>
<text:p text:style-name="P60"/>
<text:p text:style-name="P61">Mentor Signature<text:tab/><text:tab/><text:tab/><text:tab/><text:tab/><text:tab/><text:s text:c="3"/>Project Guide Signature</text:p>
<text:p text:style-name="Normal"/>
</office:text></office:body>"""


def render_content_xml(template_xml: str, report: Report) -> str:
    prefix = template_xml.split("<office:body>", 1)[0]
    return prefix + body_xml(report) + "</office:document-content>"


def write_odt_report(template_path: Path, destination: Path, content_xml: str) -> None:
    with ZipFile(template_path, "r") as source_zip, ZipFile(destination, "w") as target_zip:
        for info in source_zip.infolist():
            data = source_zip.read(info.filename)
            if info.filename == "content.xml":
                data = content_xml.encode("utf-8")
            compress_type = ZIP_STORED if info.filename == "mimetype" else ZIP_DEFLATED
            target_zip.writestr(info.filename, data, compress_type=compress_type)


def write_summary() -> None:
    summary_path = OUTPUT_DIR / "README.md"
    lines = [
        "# TerraInsights Weekly Reports",
        "",
        "Generated 12 weekly ODT reports from the provided minor-project template.",
        "",
        "Assumptions used:",
        "- Project title set to TerraInsights: Sustainable Fertilizer Usage Optimizer for Higher Yield.",
        "- Group ID and Branch/Section kept as editable placeholders.",
        "- Date ranges are mapped across 12 weekly slots ending on 05 Apr 2026.",
        "- Git activity reflects the current local repository snapshot, which primarily uses `main`.",
        "",
        "Generated files:",
    ]
    for report in REPORTS:
        lines.append(f"- Week_{report.week:02d}_TerraInsights_Report.odt")
    summary_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    template_xml = None
    with ZipFile(TEMPLATE_ODT, "r") as zip_file:
        template_xml = zip_file.read("content.xml").decode("utf-8")

    for report in REPORTS:
        out_path = OUTPUT_DIR / f"Week_{report.week:02d}_TerraInsights_Report.odt"
        content_xml = render_content_xml(template_xml, report)
        write_odt_report(TEMPLATE_ODT, out_path, content_xml)

    write_summary()
    print(f"Generated {len(REPORTS)} reports in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
