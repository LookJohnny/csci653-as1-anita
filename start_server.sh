#!/bin/bash
# Ani - AI Voice Companion Server Start Script for macOS

echo "================================"
echo "  Starting Ani Server (macOS)"
echo "================================"

# Check if .env file exists
if [ ! -f .env ]; then
    echo "ERROR: .env file not found!"
    echo "Please copy .env.example to .env and configure your API keys."
    exit 1
fi

# Check if CLAUDE_API_KEY is set
if grep -q "your-claude-api-key-here" .env; then
    echo "WARNING: CLAUDE_API_KEY not configured in .env file"
    echo "Please edit .env and set your Claude API key"
    exit 1
fi

# Start the server
echo "Starting FastAPI server on http://localhost:8000"
python3.12 main_full.py
