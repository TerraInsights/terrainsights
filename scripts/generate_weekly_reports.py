from __future__ import annotations

from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED, ZIP_STORED
from xml.sax.saxutils import escape
from PIL import Image, ImageDraw, ImageFont


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
    required_diagram: str
    required_diagram_note: str
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
    diagram_svg_name: str
    diagram_nodes: list[str]
    diagram_edges: list[tuple[int, int]]
    diagram_edge_labels: list[str]


REPORTS = [
    Report(
        week=1,
        date_range="12 Jan 2026 - 18 Jan 2026",
        sprint="Sprint 1 of 6",
        sprint_goal="Finalize project scope, sustainable farming problem statement, and initial system architecture for TerraInsights.",
        status="On Track (Green)",
        diagrams_completed="Completed the problem context diagram, the core use case diagram, and a high-level activity flow to show how a farmer will enter soil data and receive a fertilizer recommendation from TerraInsights.",
        required_diagram="Use Case Diagram",
        required_diagram_note="Shows the Farmer actor interacting with the dashboard, recommendation engine, educational module, and scheme/store support features.",
        diagrams_revised="Initial draft only; no revisions yet.",
        oo_concept="Applied modular decomposition by separating the system into ML, backend API, and frontend presentation layers so each module can evolve independently.",
        jira_tasks="TI-101 scope finalization, TI-102 technology stack review, TI-103 repository initialization checklist.",
        active_branches="main",
        merged_prs="N/A - initial prototype work tracked directly on local main.",
        cicd_status="Repository initialized; manual checklist review completed; formal CI pipeline not configured yet.",
        total_tests="0",
        pass_rate="N/A",
        key_bug="No code bug this week; the main issue identified was refining the problem scope to keep the project realistic for a minor project timeline.",
        next_goal_a="Prepare detailed UML artifacts and sprint plan for six development sprints.",
        next_goal_b="Study the fertilizer dataset and map required input/output fields for the ML workflow.",
        diagram_svg_name="Week_01_Use_Case_Diagram.svg",
        diagram_nodes=["Farmer", "TerraInsights Dashboard", "Recommendation Engine", "AgroGuide", "Govt Schemes", "Store"],
        diagram_edges=[(0, 1), (1, 2), (1, 3), (1, 4), (1, 5)],
        diagram_edge_labels=["uses", "submits farm data", "opens guide", "checks eligibility", "views products"],
    ),
    Report(
        week=2,
        date_range="19 Jan 2026 - 25 Jan 2026",
        sprint="Sprint 1 of 6",
        sprint_goal="Complete design documentation and convert requirements into a clear implementation plan.",
        status="On Track (Green)",
        diagrams_completed="Prepared a draft class diagram, a sequence diagram for the recommendation request flow, and a clearer module interaction sketch connecting ML, API, and UI responsibilities.",
        required_diagram="Sequence Diagram",
        required_diagram_note="Captures the request path from Farmer input to backend prediction and recommendation response.",
        diagrams_revised="Use case diagram revised after adding AgroGuide, Govt Schemes, and Store support modules.",
        oo_concept="Used separation of concerns by defining independent responsibilities for the UI, API, persistence, and ML pipeline to keep the design maintainable.",
        jira_tasks="TI-104 implementation plan drafting, TI-105 functional module breakdown, TI-106 data field mapping.",
        active_branches="main",
        merged_prs="N/A - local prototype planning stage.",
        cicd_status="Documentation and implementation plan reviewed manually; no automated build configured yet.",
        total_tests="2",
        pass_rate="100",
        key_bug="Resolved a requirement mismatch where the dashboard originally needed fewer inputs than the dataset columns required.",
        next_goal_a="Start dataset exploration and preprocessing strategy for model training.",
        next_goal_b="Set up the ML training script and choose the initial classification model.",
        diagram_svg_name="Week_02_Sequence_Diagram.svg",
        diagram_nodes=["Farmer", "Frontend UI", "FastAPI Backend", "ML Model"],
        diagram_edges=[(0, 1), (1, 2), (2, 3), (3, 2), (2, 1)],
        diagram_edge_labels=["enters values", "POST request", "predict()", "label output", "response payload"],
    ),
    Report(
        week=3,
        date_range="26 Jan 2026 - 01 Feb 2026",
        sprint="Sprint 2 of 6",
        sprint_goal="Understand the fertilizer dataset and prepare a reusable ML training workflow.",
        status="On Track (Green)",
        diagrams_completed="Completed a component diagram for ML-backend-frontend interaction and a preprocessing workflow diagram showing how raw agricultural data is prepared before model training.",
        required_diagram="Component Diagram",
        required_diagram_note="Explains how dataset processing, model training, backend serving, and frontend consumption connect as separate components.",
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
        diagram_svg_name="Week_03_Component_Diagram.svg",
        diagram_nodes=["Dataset CSV", "Training Script", "Saved ML Model", "FastAPI Backend", "React Frontend"],
        diagram_edges=[(0, 1), (1, 2), (2, 3), (3, 4)],
        diagram_edge_labels=["loads data", "trains + saves", "loaded by", "served to"],
    ),
    Report(
        week=4,
        date_range="02 Feb 2026 - 08 Feb 2026",
        sprint="Sprint 2 of 6",
        sprint_goal="Train the first working ML model and prepare backend data storage foundations.",
        status="On Track (Green)",
        diagrams_completed="Created the local deployment diagram and updated the prediction sequence so it now includes history logging into SQLite after each successful recommendation.",
        required_diagram="Deployment Diagram",
        required_diagram_note="Shows the local machine hosting the frontend, backend, database, and trained model artifact during development.",
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
        diagram_svg_name="Week_04_Deployment_Diagram.svg",
        diagram_nodes=["Developer Machine", "React Frontend", "FastAPI Backend", "SQLite Database", "ML Model Artifact"],
        diagram_edges=[(0, 1), (0, 2), (2, 3), (2, 4)],
        diagram_edge_labels=["hosts", "runs", "writes history", "loads model"],
    ),
    Report(
        week=5,
        date_range="09 Feb 2026 - 15 Feb 2026",
        sprint="Sprint 3 of 6",
        sprint_goal="Develop the prediction API and integrate the trained model into backend execution.",
        status="On Track (Green)",
        diagrams_completed="Finished the backend package diagram and documented the API request lifecycle so the prediction service, database session, and history storage responsibilities are easy to trace.",
        required_diagram="Package Diagram",
        required_diagram_note="Organizes backend files such as main, models, database, and ML assets into a clean package view.",
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
        diagram_svg_name="Week_05_Package_Diagram.svg",
        diagram_nodes=["backend", "main.py", "database.py", "models.py", "ml", "fertilizer_model.pkl"],
        diagram_edges=[(0, 1), (0, 2), (0, 3), (4, 5), (1, 5), (1, 2), (1, 3)],
        diagram_edge_labels=["contains", "contains", "contains", "stores", "loads", "opens session", "uses ORM"],
    ),
    Report(
        week=6,
        date_range="16 Feb 2026 - 22 Feb 2026",
        sprint="Sprint 3 of 6",
        sprint_goal="Stabilize backend payload handling and prepare the application for frontend integration.",
        status="At Risk (Yellow)",
        diagrams_completed="Expanded the backend sequence diagram to include request validation, model inference, database write-back, and structured response return after each prediction call.",
        required_diagram="Class Diagram",
        required_diagram_note="Represents key backend entities such as PredictionInput and PredictionHistory along with their responsibilities.",
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
        diagram_svg_name="Week_06_Class_Diagram.svg",
        diagram_nodes=["PredictionInput", "PredictionHistory"],
        diagram_edges=[(0, 1)],
        diagram_edge_labels=["creates record for"],
    ),
    Report(
        week=7,
        date_range="23 Feb 2026 - 01 Mar 2026",
        sprint="Sprint 4 of 6",
        sprint_goal="Build the frontend shell with navigation, routing, and foundational pages for the user journey.",
        status="On Track (Green)",
        diagrams_completed="Prepared the frontend navigation flow diagram and a page-level component breakdown to explain how routing connects landing, auth, dashboard, profile, and supporting pages.",
        required_diagram="Navigation / Activity Diagram",
        required_diagram_note="Shows the user journey through the main pages after the frontend shell was introduced.",
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
        diagram_svg_name="Week_07_Activity_Diagram.svg",
        diagram_nodes=["Open App", "Landing Page", "Auth Page", "Dashboard", "Profile", "AgroGuide", "Govt Schemes", "Store"],
        diagram_edges=[(0, 1), (1, 2), (2, 3), (3, 4), (3, 5), (3, 6), (3, 7)],
        diagram_edge_labels=["launch", "navigate", "login success", "view account", "learn", "check support", "shop"],
    ),
    Report(
        week=8,
        date_range="02 Mar 2026 - 08 Mar 2026",
        sprint="Sprint 4 of 6",
        sprint_goal="Integrate the dashboard with the backend and make the recommendation flow usable end to end.",
        status="At Risk (Yellow)",
        diagrams_completed="Completed a detailed dashboard-to-API sequence diagram and refined the input model mapping so the frontend form can drive ML inference reliably.",
        required_diagram="Detailed Sequence Diagram",
        required_diagram_note="Captures numeric conversion, API request flow, backend inference, and result rendering in the dashboard.",
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
        diagram_svg_name="Week_08_Detailed_Sequence_Diagram.svg",
        diagram_nodes=["Farmer", "Dashboard", "Backend", "ML Model", "SQLite"],
        diagram_edges=[(0, 1), (1, 1), (1, 2), (2, 3), (3, 2), (2, 4), (2, 1), (1, 0)],
        diagram_edge_labels=["fills form", "casts numbers", "POST /predict", "infer", "prediction", "save history", "result", "display"],
    ),
    Report(
        week=9,
        date_range="09 Mar 2026 - 15 Mar 2026",
        sprint="Sprint 5 of 6",
        sprint_goal="Complete the content modules that support the recommendation experience beyond core prediction.",
        status="On Track (Green)",
        diagrams_completed="Prepared the feature package diagram for Store, AgroGuide, and Govt Schemes pages and described how these pages extend the core recommendation workflow.",
        required_diagram="Feature Component Diagram",
        required_diagram_note="Highlights how supporting modules connect to the shared frontend shell without affecting backend prediction logic.",
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
        diagram_svg_name="Week_09_Feature_Component_Diagram.svg",
        diagram_nodes=["App Router", "Dashboard", "Store Page", "AgroGuide Page", "Govt Schemes Page"],
        diagram_edges=[(0, 1), (0, 2), (0, 3), (0, 4)],
        diagram_edge_labels=["route", "route", "route", "route"],
    ),
    Report(
        week=10,
        date_range="16 Mar 2026 - 22 Mar 2026",
        sprint="Sprint 5 of 6",
        sprint_goal="Polish the complete product experience and reduce integration rough edges before final validation.",
        status="On Track (Green)",
        diagrams_completed="Revised the deployment and integration diagrams so they now reflect the full localhost execution flow across frontend, backend, database, and ML model files.",
        required_diagram="Integrated Deployment Diagram",
        required_diagram_note="Presents the polished application as a connected local system ready for demonstration.",
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
        diagram_svg_name="Week_10_Integrated_Deployment_Diagram.svg",
        diagram_nodes=["Browser", "React App", "FastAPI Service", "ML Model", "SQLite"],
        diagram_edges=[(0, 1), (1, 2), (2, 3), (2, 4)],
        diagram_edge_labels=["renders UI", "API calls", "loads for inference", "stores history"],
    ),
    Report(
        week=11,
        date_range="23 Mar 2026 - 29 Mar 2026",
        sprint="Sprint 6 of 6",
        sprint_goal="Carry out final validation, confirm prediction history logging, and strengthen project documentation.",
        status="On Track (Green)",
        diagrams_completed="Completed the final revision set for sequence, component, and deployment diagrams so the documentation now matches the implemented TerraInsights prototype more closely.",
        required_diagram="History Flow Sequence Diagram",
        required_diagram_note="Focuses on how prediction history is saved and later retrieved for review.",
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
        diagram_svg_name="Week_11_History_Flow_Sequence_Diagram.svg",
        diagram_nodes=["Dashboard", "Backend", "SQLite"],
        diagram_edges=[(0, 1), (1, 2), (2, 1), (1, 0), (0, 1), (1, 2), (2, 1), (1, 0)],
        diagram_edge_labels=["prediction request", "insert row", "save ok", "recommendation", "history request", "read rows", "records", "history list"],
    ),
    Report(
        week=12,
        date_range="30 Mar 2026 - 05 Apr 2026",
        sprint="Sprint 6 of 6",
        sprint_goal="Finalize the TerraInsights prototype, consolidate submission material, and prepare for mentor review.",
        status="On Track (Green)",
        diagrams_completed="Prepared the final documentation pack containing consolidated UML references, week-wise implementation mapping, and the final project structure summary for submission.",
        required_diagram="Final System Overview Diagram",
        required_diagram_note="Provides a concise end-state overview of all major TerraInsights modules for mentor review.",
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
        diagram_svg_name="Week_12_Final_System_Overview_Diagram.svg",
        diagram_nodes=["Farmer", "React Frontend", "FastAPI Backend", "Trained Model", "SQLite History", "Guide + Schemes + Store"],
        diagram_edges=[(0, 1), (1, 2), (2, 3), (2, 4), (1, 5)],
        diagram_edge_labels=["interacts with", "calls", "predicts with", "stores in", "navigates to"],
    ),
]


def span(style: str, text: str) -> str:
    return f'<text:span text:style-name="{style}">{escape(text)}</text:span>'


def diagram_png_name(report: Report) -> str:
    return report.diagram_svg_name.replace(".svg", ".png")


def diagram_odt_path(report: Report) -> str:
    return f"Pictures/{diagram_png_name(report)}"


def diagram_frame_xml(report: Report) -> str:
    href = diagram_odt_path(report)
    return (
        '<text:p text:style-name="P60">Required Diagram Image</text:p>'
        '<text:p text:style-name="P60">'
        f'<draw:frame draw:name="Week{report.week}Diagram" text:anchor-type="paragraph" svg:width="6.5in" svg:height="3.9in" draw:z-index="0">'
        f'<draw:image xlink:href="{href}" xlink:type="simple" xlink:show="embed" xlink:actuate="onLoad"/>'
        "</draw:frame>"
        "</text:p>"
    )


def body_xml(report: Report) -> str:
    pass_rate_text = report.pass_rate if report.pass_rate == "N/A" else f"{report.pass_rate}%"
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
<text:list-item><text:p text:style-name="P17">{span("T18", "Detailed Progress:")}{span("T19", f" {detailed_progress(report)}")}</text:p></text:list-item>
</text:list>
<text:p text:style-name="P26">2. UML &amp; OOAD Progress</text:p>
<text:list text:style-name="LFO2" text:continue-numbering="true">
<text:list-item><text:p text:style-name="P27">{span("T28", "Diagrams Completed this week:")}{span("T29", f" {report.diagrams_completed}")}</text:p></text:list-item>
<text:list-item><text:p text:style-name="P30">{span("T31", "Diagrams Revised:")}{span("T32", f" {report.diagrams_revised}")}</text:p></text:list-item>
<text:list-item><text:p text:style-name="P33">{span("T34", "Required Diagram Added:")}{span("T35", f" {report.required_diagram} - {report.required_diagram_note}")}</text:p></text:list-item>
<text:list-item><text:p text:style-name="P33">{span("T34", "OO Concept Applied:")}{span("T35", f" {report.oo_concept}")}</text:p></text:list-item>
</text:list>
{diagram_frame_xml(report)}
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
<text:list-item><text:p text:style-name="P51">{span("T52", "Pass Rate:")}{span("T53", f" {pass_rate_text}")}</text:p></text:list-item>
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


def render_manifest_xml(template_manifest: str, report: Report) -> str:
    closing = "</manifest:manifest>"
    insert = f'<manifest:file-entry manifest:media-type="image/png" manifest:full-path="{diagram_odt_path(report)}"/>'
    return template_manifest.replace(closing, insert + closing)


def write_odt_report(template_path: Path, destination: Path, report: Report, content_xml: str, manifest_xml: str, png_bytes: bytes) -> None:
    with ZipFile(template_path, "r") as source_zip, ZipFile(destination, "w") as target_zip:
        for info in source_zip.infolist():
            data = source_zip.read(info.filename)
            if info.filename == "content.xml":
                data = content_xml.encode("utf-8")
            elif info.filename == "META-INF/manifest.xml":
                data = manifest_xml.encode("utf-8")
            compress_type = ZIP_STORED if info.filename == "mimetype" else ZIP_DEFLATED
            target_zip.writestr(info.filename, data, compress_type=compress_type)
        target_zip.writestr(diagram_odt_path(report), png_bytes, compress_type=ZIP_DEFLATED)


def write_summary() -> None:
    summary_path = OUTPUT_DIR / "README.md"
    diagrams_dir = OUTPUT_DIR / "diagrams"
    lines = [
        "# TerraInsights Weekly Reports",
        "",
        "Generated 12 weekly ODT reports from the provided minor-project template.",
        "Each report is slightly more descriptive and has a matching weekly required-diagram file.",
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
    lines.extend(
        [
            "",
            "Diagram files:",
        ]
    )
    for report in REPORTS:
        lines.append(f"- diagrams/{diagram_png_name(report)}")
    summary_path.write_text("\n".join(lines), encoding="utf-8")
    diagrams_dir.mkdir(exist_ok=True)
    for report in REPORTS:
        (diagrams_dir / diagram_png_name(report)).write_bytes(render_png(report))


def escape_xml(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def render_svg(report: Report) -> str:
    width = 1400
    height = 780
    box_w = 220
    box_h = 72
    count = len(report.diagram_nodes)
    cols = 3 if count > 4 else count
    rows = (count + cols - 1) // cols
    gap_x = 150
    gap_y = 130
    start_x = 80
    start_y = 140

    positions: list[tuple[int, int]] = []
    for i in range(count):
        row = i // cols
        col = i % cols
        x = start_x + col * (box_w + gap_x)
        y = start_y + row * (box_h + gap_y)
        positions.append((x, y))

    def center(idx: int) -> tuple[int, int]:
        x, y = positions[idx]
        return x + box_w // 2, y + box_h // 2

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        "<defs>",
        '<marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto" markerUnits="strokeWidth">',
        '<path d="M0,0 L0,6 L9,3 z" fill="#2f5d50" />',
        "</marker>",
        "</defs>",
        '<rect width="100%" height="100%" fill="#f6fbf8" />',
        '<rect x="28" y="24" width="1344" height="730" rx="24" ry="24" fill="none" stroke="#b8d8c6" stroke-width="2" />',
        f'<text x="{width/2}" y="48" text-anchor="middle" font-size="28" font-family="Segoe UI, Arial, sans-serif" fill="#183b2d" font-weight="700">Week {report.week} - {escape_xml(report.required_diagram)}</text>',
        f'<text x="{width/2}" y="82" text-anchor="middle" font-size="16" font-family="Segoe UI, Arial, sans-serif" fill="#476457">{escape_xml(report.required_diagram_note)}</text>',
        f'<text x="70" y="730" font-size="15" font-family="Segoe UI, Arial, sans-serif" fill="#476457">Practical note: Diagram aligned with the implemented TerraInsights modules for weekly documentation.</text>',
    ]

    for idx, (src, dst) in enumerate(report.diagram_edges):
        x1, y1 = center(src)
        x2, y2 = center(dst)
        parts.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#2f5d50" stroke-width="3" marker-end="url(#arrow)" />'
        )
        label = report.diagram_edge_labels[idx] if idx < len(report.diagram_edge_labels) else ""
        if label:
            mx = (x1 + x2) / 2
            my = (y1 + y2) / 2 - 8
            parts.append(
                f'<rect x="{mx - 48}" y="{my - 16}" width="96" height="24" rx="8" ry="8" fill="#ffffff" stroke="#b8d8c6" stroke-width="1" />'
            )
            parts.append(
                f'<text x="{mx}" y="{my}" text-anchor="middle" dominant-baseline="middle" font-size="12" font-family="Segoe UI, Arial, sans-serif" fill="#244739">{escape_xml(label)}</text>'
            )

    for idx, label in enumerate(report.diagram_nodes):
        x, y = positions[idx]
        fill = "#dff4e8"
        if "Backend" in label or "Service" in label:
            fill = "#dceeff"
        elif "Model" in label:
            fill = "#fff0cf"
        elif "Database" in label or "SQLite" in label or "History" in label:
            fill = "#f2e5ff"
        elif "Farmer" in label or "Browser" in label:
            fill = "#ffe4e1"
        parts.append(
            f'<rect x="{x}" y="{y}" rx="16" ry="16" width="{box_w}" height="{box_h}" fill="{fill}" stroke="#2f5d50" stroke-width="2.5" />'
        )
        words = label.split()
        lines: list[str] = []
        current = ""
        for word in words:
            test = f"{current} {word}".strip()
            if len(test) <= 18:
                current = test
            else:
                lines.append(current)
                current = word
        if current:
            lines.append(current)
        base_y = y + 30 - ((len(lines) - 1) * 10)
        for line_no, line in enumerate(lines):
            parts.append(
                f'<text x="{x + box_w/2}" y="{base_y + line_no*20}" text-anchor="middle" font-size="18" font-family="Segoe UI, Arial, sans-serif" fill="#183b2d" font-weight="600">{escape_xml(line)}</text>'
            )

    parts.append("</svg>")
    return "\n".join(parts)


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except Exception:
            continue
    return ImageFont.load_default()


def render_png(report: Report) -> bytes:
    width, height = 1400, 780
    box_w, box_h = 230, 80
    count = len(report.diagram_nodes)
    cols = 3 if count > 4 else count
    gap_x, gap_y = 145, 130
    start_x, start_y = 80, 140

    image = Image.new("RGB", (width, height), "#f6fbf8")
    draw = ImageDraw.Draw(image)
    title_font = load_font(30, bold=True)
    subtitle_font = load_font(16)
    node_font = load_font(18, bold=True)
    label_font = load_font(12)
    note_font = load_font(15)

    positions: list[tuple[int, int]] = []
    for i in range(count):
        row = i // cols
        col = i % cols
        positions.append((start_x + col * (box_w + gap_x), start_y + row * (box_h + gap_y)))

    def center(idx: int) -> tuple[int, int]:
        x, y = positions[idx]
        return x + box_w // 2, y + box_h // 2

    draw.rounded_rectangle((28, 24, 1372, 754), radius=24, outline="#b8d8c6", width=2)
    draw.text((width // 2, 48), f"Week {report.week} - {report.required_diagram}", anchor="mm", fill="#183b2d", font=title_font)
    draw.text((width // 2, 82), report.required_diagram_note, anchor="mm", fill="#476457", font=subtitle_font)
    draw.text((70, 730), "Practical note: Diagram aligned with the implemented TerraInsights modules for weekly documentation.", fill="#476457", font=note_font)

    for idx, (src, dst) in enumerate(report.diagram_edges):
        x1, y1 = center(src)
        x2, y2 = center(dst)
        draw.line((x1, y1, x2, y2), fill="#2f5d50", width=3)
        dx, dy = x2 - x1, y2 - y1
        if dx == 0 and dy == 0:
            draw.arc((x1 - 35, y1 - 35, x1 + 35, y1 + 35), start=40, end=320, fill="#2f5d50", width=3)
        else:
            import math
            ang = math.atan2(dy, dx)
            arrow_len = 12
            left = (
                x2 - arrow_len * math.cos(ang) + 6 * math.sin(ang),
                y2 - arrow_len * math.sin(ang) - 6 * math.cos(ang),
            )
            right = (
                x2 - arrow_len * math.cos(ang) - 6 * math.sin(ang),
                y2 - arrow_len * math.sin(ang) + 6 * math.cos(ang),
            )
            draw.polygon([(x2, y2), left, right], fill="#2f5d50")
        label = report.diagram_edge_labels[idx] if idx < len(report.diagram_edge_labels) else ""
        if label:
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2 - 10
            draw.rounded_rectangle((mx - 52, my - 12, mx + 52, my + 12), radius=8, fill="#ffffff", outline="#b8d8c6", width=1)
            draw.text((mx, my), label, anchor="mm", fill="#244739", font=label_font)

    for idx, label in enumerate(report.diagram_nodes):
        x, y = positions[idx]
        fill = "#dff4e8"
        if "Backend" in label or "Service" in label:
            fill = "#dceeff"
        elif "Model" in label:
            fill = "#fff0cf"
        elif "Database" in label or "SQLite" in label or "History" in label:
            fill = "#f2e5ff"
        elif "Farmer" in label or "Browser" in label:
            fill = "#ffe4e1"
        draw.rounded_rectangle((x, y, x + box_w, y + box_h), radius=16, fill=fill, outline="#2f5d50", width=3)
        words = label.split()
        lines: list[str] = []
        current = ""
        for word in words:
            test = f"{current} {word}".strip()
            if len(test) <= 18:
                current = test
            else:
                lines.append(current)
                current = word
        if current:
            lines.append(current)
        base_y = y + 28 - ((len(lines) - 1) * 11)
        for i, line in enumerate(lines):
            draw.text((x + box_w / 2, base_y + i * 22), line, anchor="mm", fill="#183b2d", font=node_font)

    output = BytesIO()
    image.save(output, format="PNG")
    return output.getvalue()


def detailed_progress(report: Report) -> str:
    pass_rate_part = report.pass_rate if report.pass_rate == "N/A" else f"{report.pass_rate}%"
    return (
        f"This week the project concentrated on {report.sprint_goal.lower()} "
        f"The team completed work around {report.diagrams_completed.lower()} "
        f"In practical terms, the technical tasks covered {report.jira_tasks}, while testing status moved to "
        f"{report.total_tests} checks with a {pass_rate_part} pass rate. "
        f"The main observation for the week was: {report.key_bug}"
    )


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    template_xml = None
    template_manifest = None
    with ZipFile(TEMPLATE_ODT, "r") as zip_file:
        template_xml = zip_file.read("content.xml").decode("utf-8")
        template_manifest = zip_file.read("META-INF/manifest.xml").decode("utf-8")

    for report in REPORTS:
        out_path = OUTPUT_DIR / f"Week_{report.week:02d}_TerraInsights_Report.odt"
        content_xml = render_content_xml(template_xml, report)
        manifest_xml = render_manifest_xml(template_manifest, report)
        png_bytes = render_png(report)
        write_odt_report(TEMPLATE_ODT, out_path, report, content_xml, manifest_xml, png_bytes)

    write_summary()
    print(f"Generated {len(REPORTS)} reports in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
