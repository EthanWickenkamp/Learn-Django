#!/bin/bash

set -e

# Navigate to the app directory
cd /app/learn

# Ensure dependencies are installed (optional for fresh containers)
echo "Installing dependencies..."
npm install

# Start the Svelte dev server
echo "Starting Svelte development server..."
exec npm run dev -- --host
