# Notes to My Future Self Skill

A comprehensive Claude skill for building and maintaining a personal knowledge base—a searchable system of decisions, discoveries, and ongoing conversations with yourself.

## Overview

This skill helps you extract insights from long conversations with AI assistants, organize them into structured summaries, and build a cumulative knowledge base that you can reference and build upon over time.

## Key Features

- **Extract Summaries**: Convert long conversation threads into reusable markdown reference documents
- **Organize & Index**: Automatically file summaries into categories and maintain an index
- **Structured Templates**: Use consistent markdown templates for easy scanning and reference
- **Helper Scripts**: Python utilities for validating and managing your notes

## What's Included

- `SKILL.md` - Full skill documentation and workflows
- `references/` - Templates, example entries, and extraction prompts
  - `CHAT_SUMMARY_TEMPLATE.md` - Blank template for new entries
  - `EXAMPLE_ENTRY.md` - Completed example (sunscreen research)
  - `PROMPT_FOR_EXTRACTING_SUMMARIES.md` - Prompt to extract existing conversations
- `scripts/` - Helper Python utilities
  - `organize_summary.py` - Validate, extract metadata, and manage your system

## Quick Start

### 1. Extract a Summary from an Existing Conversation

1. Have a long conversation with an AI about a topic
2. Ask: "I need the prompt to extract a chat summary"
3. Copy the extraction prompt from `references/PROMPT_FOR_EXTRACTING_SUMMARIES.md`
4. Paste it into your original conversation thread
5. Save the resulting markdown to your Notes folder

### 2. Create a New Entry

1. Use the template from `references/CHAT_SUMMARY_TEMPLATE.md`
2. Fill in the sections with your decision/research
3. Save to the appropriate category folder
4. Run the helper script to validate and index it

### 3. Reference Your Notes

When starting a new conversation, paste your summary at the top:

```
Here's my background research on [TOPIC] from previous conversations:

[PASTE YOUR MARKDOWN SUMMARY HERE]

Now I'd like to [describe what you want to do next]...
```

## Categories

Your notes are organized into these categories:

- **Household_Maintenance**: Home systems, filters, schedules
- **Product_Reviews_Decisions**: Brands tested, what worked/didn't, why
- **Health_Wellness**: Medications, supplements, wellness practices
- **Recipes_Cooking**: Dishes made, modifications, feedback
- **Tech_Setups_Tools**: Tools configured, settings, troubleshooting
- **Learning_Exploration**: Courses, AI tools tested, experiments
- **Emergency_Preparedness**: Safety planning, supplies, procedures

## Usage with Claude

This skill is designed to work seamlessly with Claude. When you need help managing your Notes to My Future Self, simply ask Claude and invoke this skill.

## Design Philosophy

This workflow prevents context bloat in long conversations by:
1. You explore with AI (long back-and-forth conversations)
2. Claude extracts insights into a structured summary
3. You organize summaries into categories
4. You reference old decisions without re-researching
5. You iterate by seeding new conversations with past knowledge
6. Your personal knowledge compounds over time as a searchable system

## File Structure

```
notes-to-future-self-skill/
├── README.md
├── SKILL.md
├── references/
│   ├── CHAT_SUMMARY_TEMPLATE.md
│   ├── EXAMPLE_ENTRY.md
│   └── PROMPT_FOR_EXTRACTING_SUMMARIES.md
└── scripts/
    └── organize_summary.py
```

## Tips for Best Results

**When extracting summaries:**
- Use the provided prompt exactly as given
- Paste it into the same conversation you want to summarize
- Include specific product names, prices, and details
- The AI will create tables automatically

**When organizing:**
- Categories are flexible—pick the best fit
- Add review dates so you know when to revisit decisions
- Include your personal constraints (budget, health, lifestyle)

**For future conversations:**
- Paste your summary at the top of new conversations
- Say something like "Here's my background, now I want to explore..."
- This keeps context focused while leveraging your past thinking

## Installation & Setup

### Option 1: Using Claude Code (Recommended)

If you use Claude Code, you can add this as a skill:

1. Clone the repository or download the skill folder
2. Move the `notes-to-future-self-skill` folder to your Claude Code skills directory
3. Restart Claude Code to load the skill
4. Invoke the skill by asking Claude Code for help with your Notes

### Option 2: Manual Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/bladngal/notes-to-future-self-skill.git
   cd notes-to-future-self-skill
   ```

2. **Create your Notes directory structure:**
   Choose where you want to store your notes (e.g., `~/Notes-To-My-Future-Self`, `~/my-notes`, `/path/to/your/notes`, etc.)
   ```bash
   mkdir -p ~/Notes-To-My-Future-Self/{Household_Maintenance,Product_Reviews_Decisions,Health_Wellness,Recipes_Cooking,Tech_Setups_Tools,Learning_Exploration,Emergency_Preparedness}
   ```

3. **Copy templates to your Notes folder:**
   ```bash
   cp references/CHAT_SUMMARY_TEMPLATE.md ~/Notes-To-My-Future-Self/CHAT_SUMMARY_TEMPLATE.md
   cp references/PROMPT_FOR_EXTRACTING_SUMMARIES.md ~/Notes-To-My-Future-Self/PROMPT_FOR_EXTRACTING_SUMMARIES.md
   ```

4. **Set up the helper script (optional):**
   ```bash
   # Make the script executable
   chmod +x scripts/organize_summary.py

   # Run it with --help to see available commands
   python3 scripts/organize_summary.py
   ```

5. **Configure the script path (if needed):**
   The script will automatically look for your Notes folder in the parent directories. If you want to use a custom location, set the environment variable:
   ```bash
   # Point to your notes folder (change the path to match your setup)
   export NOTES_DIR=~/Notes-To-My-Future-Self
   ```

## Quick Start

### 1. Extract a Summary from an Existing Conversation

1. Have a long conversation with an AI about a topic
2. Ask: "I need the prompt to extract a chat summary"
3. Copy the extraction prompt from `references/PROMPT_FOR_EXTRACTING_SUMMARIES.md`
4. Paste it into your original conversation
5. Save the resulting markdown file to your Notes folder
6. Ask Claude Code: "Help me save this summary to my Notes"

### 2. Create a New Entry from Scratch

1. Copy `references/CHAT_SUMMARY_TEMPLATE.md`
2. Fill in the sections with your decision or research
3. Save to the appropriate category folder
4. Ask Claude Code: "Help me organize this file into my Notes system"

### 3. Reference Your Notes in Future Conversations

```
Here's my background research on [TOPIC] from previous conversations:

[PASTE YOUR MARKDOWN SUMMARY HERE]

Now I'd like to [describe what you want to do next]...
```

## Using the Helper Script

The `organize_summary.py` script provides utilities for managing your Notes:

```bash
# Validate a summary file has required sections
python3 scripts/organize_summary.py validate path/to/file.md

# Extract metadata from a summary
python3 scripts/organize_summary.py extract path/to/file.md

# List all files in a category
python3 scripts/organize_summary.py list Product_Reviews_Decisions
```

## Contributing

We'd love your help! See [CONTRIBUTING.md](CONTRIBUTING.md) for ways to contribute, including:
- Reporting bugs or suggesting improvements
- Improving documentation
- Sharing your workflow or templates
- Enhancing the helper script

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

*Created: 2026-01-26*
*Designed for Claude and Cowork*
*Visit the [CHANGELOG](CHANGELOG.md) to see what's been added and changed*
