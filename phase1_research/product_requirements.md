# Product Requirements Document: ChatGPT Evaluation Mode

## 1. Functional Requirements

### **FR1: Intent Classification & Stakes Detection**
- The system MUST analyze user prompts to categorize intent (Creative, Technical, Factual, etc.).
- The system MUST assign a "Stakes Level" (Low, Medium, High) to each interaction.

### **FR2: Automated Source Auditing**
- The system MUST extract all URLs, DOIs, and citations from AI responses.
- The system MUST verify the live status of these links and flag hallucinated sources.

### **FR3: De-biasing UI Toggle**
- The system MUST provide a "Neutral View" that removes bolding, bullets, and persuasive adjectives.

### **FR4: Human Accountability Workflow**
- The system MUST require a "Sign-Off" on specific claims for High-Stakes categories before unlocking the "Copy" button.

### **FR5: Confidence Heatmap**
- The system MUST visualize the AI's internal confidence score for different segments of the response.

---

## 2. UX/UI Requirements

### **UR1: Dual-Pane Layout**
- The primary interface MUST display the AI response in one pane and the "Evaluation Bench" in the other.

### **UR2: Visual Indicators**
- Source verification status MUST be color-coded (🟢/🟡/🔴).
- High-stakes warnings MUST be prominent and non-dismissible without an action.

### **UR3: Meaningful Friction**
- For High-Stakes tasks, a "Thinking Delay" (3-5 seconds) MUST be implemented before verification tools are enabled.

---

## 3. Backend & Technical Requirements

### **TR1: Orchestration Layer**
- The backend MUST support multi-model orchestration (e.g., GPT-4o for generation, Claude 3.5 for auditing).

### **TR2: Fact-Checking Integration**
- The system MUST integrate with Serper.dev or Google Search API for real-time grounding.

### **TR3: Evaluation Database**
- The system MUST store a "Verification Ledger" for all high-stakes interactions.
