#!/bin/bash

set -e

cd /app/learn
echo "Installing dependencies..."
npm install

echo "Starting Svelte development server..."
exec npm run dev -- --host
