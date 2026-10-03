# 🤖 Agentic Assistant - Design Doc V1

## 1. Overview

A stateless, tool-based personal assistant designed to automate routine digital tasks. The system relies on a central Orchestrator to route requests to specialized agents and synthesize results. It prioritizes safety through scoped execution environments and restricted tool access.

## 2. Core Principles

- **Stateless Architecture:** No persistent memory between sessions; context is provided via UI or current session buffer.

- **Tool-Based Execution:** Agents interact with the world exclusively through defined APIs and tools.

- **Simple UX:** A minimalist interface that reduces cognitive load and focuses on clear action

## 3. System Architecture

### 3.1 High-Level Diagram

TODO

### 3.2 Detailed Agent Specifications

#### A. The Orchestrator

**Role:** The central "brain" and router of the entire system. It receives the user's natural language request, interprets the intent, and decides the optimal execution strategy. Rather than executing tasks directly, it acts as a manager—breaking down complex requests into sub-tasks, delegating them to the appropriate Specialized Agents, and synthesizing their results into a final, cohesive response.

**Core Engine:** Powered by **DeepSeek V4 Pro**, chosen for its advanced reasoning, complex planning, and multi-step tool-calling capabilities.

**Key Capabilities:**

- **Intent Recognition & Routing:** Analyzes user input to determine exactly which agent (or combination of agents) is required to fulfill the request.

- **Task Decomposition:** Breaks down large, multi-part goals into a sequential or parallel workflow of smaller, agent-executable steps.

- **Result Synthesis:** Aggregates the raw data returned by the agents, resolves any conflicts, and formats it into a clear, human-readable response for the user.

#### B. Communications & Scheduling Agent

**Role:** Acts as the primary interface for managing the user's professional and personal correspondence. It handles the drafting, sending, and organizing of emails, as well as managing calendar availability and scheduling meetings seamlessly.

**Core Engine:** Powered by Qwen 3.8 Flash (Optimized for rapid tool-calling, tone adaptation, and structured data extraction).

**Key Capabilities:**

- **Email Management:** Drafts, sends, and organizes emails via integrated mail APIs (e.g., Gmail).

- **Inbox Intelligence:** Queries and filters the inbox for specific topics, senders, or action items.

- **Calendar Orchestration:** Creates events, manages availability, checks for scheduling conflicts, and sends calendar invitations.

#### C. Research & Intelligence Agent

**Role:** Responsible for gathering, parsing, and synthesizing external information. It scours the web for relevant data, extracts content from specific sources, and distills large amounts of information into actionable, concise insights for the user.

**Core Engine:** Powered by Qwen 3.8 Flash (Optimized for multi-source reasoning, fact-checking, and fast summarization).

**Key Capabilities:**

- **Web Search:** Queries search engines to find relevant links, articles, and real-time data snippets.

- **Content Extraction:** Scrapes and parses clean text from specific webpages or documents for deep analysis.

- **Information Synthesis:** Summarizes and structures extracted data into readable formats, such as bullet points or comparative tables.

#### D. Development & Code Agent

**Role:** Executes complex logic, data processing, and system-level automation. It operates within a strictly isolated sandbox to write, debug, and run code safely, allowing the system to perform computational tasks and developer workflows without risking the host environment.

**Core Engine:** Powered by Qwen 3.8 Flash (Optimized for code generation, logical debugging, and safe tool orchestration).

**Key Capabilities:**

- **Script Execution:** Writes and runs code (e.g., Python, Node.js) for data analysis, mathematical computations, or complex logical workflows.

- **System Commands:** Executes safe, whitelisted shell commands for file manipulation, environment checks, or network requests.

- **Sandboxed Processing:** Handles all heavy computation and external API calls within a restricted, ephemeral Docker environment to ensure host security.

#### E. Workspace & File Management Agent

**Role:** Acts as the digital janitor and librarian for the user's local machine. It manages local files, organizes cluttered directories, and maintains a secure local workspace to give the stateless system a form of persistent "memory" via structured files.

**Core Engine:** Powered by Qwen 3.8 Flash (Optimized for structured data formatting, file system logic, and local context management).

**Key Capabilities:**

- **Download Triage & Cleanup:** Scans directories like \~/Downloads to organize files by type/date, and proposes safe cleanup actions for old, large, or duplicate files.

- **Local Knowledge Storage:** Reads from and writes to a dedicated \~/assistant\_workspace directory to save user preferences, notes, and to-do lists across sessions.

- **File System Operations:** Securely moves, renames, and archives local files based on user-defined organizational rules.

#### F. Media & Document Processing Agent

**Role:** Specializes in ingesting, parsing, and transforming heavy or complex file formats. It handles the heavy lifting of extracting data from unstructured or dense files so the rest of the system can easily process and utilize the information.

**Core Engine:** Powered by Qwen 3.8 Flash (Optimized for multimodal understanding, precise data extraction, and structural formatting).

**Key Capabilities:**

- **Document Parsing:** Extracts clean text, tables, and specific data points from dense formats like PDFs, Word documents, and Excel/CSV files.

- **Media Transcription & OCR:** Processes audio/video transcripts and reads text from images to extract key takeaways or answer specific questions.

- **Format Conversion:** Translates files between different formats on demand (e.g., turning a messy CSV into structured JSON, or a Markdown draft into a clean PDF).

## 4. User Experience (UX) Strategy

### 4.1 UI Philosophy

* **Minimal Cognitive Load:** The interface should be clean and distraction-free, presenting only the information the user needs at any given moment.

* **Transparent Execution:** The user should always have visibility into what the system is doing. Clear, real-time status indicators (e.g., "Searching the web...", "Drafting email...", "Running script...") should keep the user informed without overwhelming them.

* **Action-Oriented Feedback:** Results and outputs should be presented clearly within the conversation flow, making it immediately obvious what was accomplished and what the user can do next.

### 4.2 UX Flow

1. **Context Input:** The user provides any relevant context or preferences for the current session.

2. **Request:** The user submits a natural language request.

3. **Routing:** The Orchestrator interprets intent and delegates to the appropriate Specialized Agent(s).

4. **Execution:** The assigned Agent(s) perform the task using their scoped tools.

5. **Synthesis:** The Orchestrator aggregates the results and presents a clear, final summary to the user..

## 5. Technical Stack (V1)

* **Core Language & Environment:** 100% Python, utilizing uv for ultra-fast package management, dependency resolution, and virtual environment handling.

* **Frontend / UI:** Streamlit (For a lightweight, Python-native, and rapid UI development experience).

* **Agent Framework:** Agno (A lightweight, Python-first framework for building, routing, and executing AI agents).

* **LLM Provider & Routing:** Powered by **OpenRouter** for unified API access and seamless model switching.

* **Orchestrator:** DeepSeek V4 Pro (For complex reasoning, planning, and task decomposition).

* **Specialized Agents:** Qwen 3.8 Flash (For fast, efficient tool-calling and localized execution).

* **Storage & State:** No database. The system remains strictly ephemeral and in-memory during execution, relying solely on the local \~/assistant\_workspace file system for any cross-session persistence.

## 6. Future Roadmap (V2 & Beyond)

* **User-Based Persistent Memory (Primary Focus):** Transition from a strictly stateless architecture to a personalized, user-specific memory system. Implement a local vector database (e.g., ChromaDB or Qdrant) tied to individual user profiles, allowing the system to securely store, retrieve, and learn from long-term preferences, historical context, and behavioral patterns across sessions.

* **Advanced Multi-Modal Interactions:** Integrate native voice-to-text and text-to-speech capabilities, allowing for hands-free operation and more natural, conversational flows alongside the text-based UI.

* **Deeper Ecosystem Integrations:** Expand beyond core email and calendar APIs to include direct, read/write integrations with communication platforms (Slack, Teams), project management tools (Notion, Linear), and local smart home/IoT APIs.

* **Adaptive Routing & Self-Optimization:** Enable the Orchestrator to learn from past successful task completions, dynamically optimizing its agent routing and tool selection over time to reduce latency and improve accuracy.

* **Collaborative Workspaces (Optional):** Allow users to securely share specific subsets of their \~/assistant\_workspace or agent configurations with team members or family for coordinated, multi-user task management.